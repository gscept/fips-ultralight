
#===============================================================================
#   ./fips ultralite [cmd]
#       install
#
#   Bootstrap ultralite sdk by downloading and unpacking to correct folders and
#   exposing it to other projects
#===============================================================================

from codecs import ignore_errors
import os, shutil, subprocess, py7zr, shutil, glob
from urllib.request import urlretrieve

from mod import log, util,settings

ULTRALIGHT_URL= 'https://github.com/ultralight-ux/Ultralight/releases/download/v{}/ultralight-sdk-{}-{}-x64.7z'
ULTRALIGHT_RELEASE = '1.2.1'
platform_dict = {'linux' : 'linux','win' : 'win', 'osx' : 'mac'}


def make_dirs(path):
    if not os.path.isdir(path):
        os.makedirs(path)

def download_ultralight(fips_dir, proj_dir):
    file_url = ULTRALIGHT_URL.format(ULTRALIGHT_RELEASE, ULTRALIGHT_RELEASE, platform_dict[util.get_host_platform()])
    target_dir = util.get_workspace_dir(fips_dir) + '/fips-build/ultralight-cache/'
    make_dirs(target_dir)
    extract_dir = target_dir + 'extract'
    if os.path.isdir(extract_dir):
        shutil.rmtree(extract_dir, ignore_errors=True)
    make_dirs(extract_dir)
    
    target_file = target_dir + 'utralite.7z'
    if not os.path.exists(target_file):
        log.info("downloading '{}'...".format(file_url))
        urlretrieve(file_url, target_file, util.url_download_hook)
    log.info("\nunpacking ... {}".format(target_file))
    archive = py7zr.SevenZipFile(target_file)
    archive.extractall(extract_dir)
    
    target_dir = util.get_workspace_dir(fips_dir) + '/fips-deploy/ultralight/'
    log.info("Copying to deploy {}".format(target_dir))
    shutil.copytree(extract_dir + '/include', target_dir + '/include', dirs_exist_ok=True)
    if os.path.isdir(extract_dir + '/lib'):
        shutil.copytree(extract_dir + '/lib', target_dir + '/lib', dirs_exist_ok=True)
    else:
        make_dirs(target_dir + '/lib')
        for lib in glob.glob(extract_dir + '/bin/*.so'):
            shutil.copy(lib, target_dir + '/lib')

    cur_cfg = settings.get(proj_dir, 'config')
    target_dir = util.get_deploy_dir(fips_dir, util.get_project_name_from_dir(proj_dir), cur_cfg)
    shutil.copytree(extract_dir + '/bin', target_dir, dirs_exist_ok=True)

    shutil.rmtree(extract_dir, ignore_errors=True)


def run(fips_dir, proj_dir, args):
    download_ultralight(fips_dir, proj_dir)

def help():
    """print 'ultralight' help"""
    log.info(log.YELLOW +
             "fips ultralight\n"
             "  Downloads and upacks a version of ultralight to the deploy folder"
             )
