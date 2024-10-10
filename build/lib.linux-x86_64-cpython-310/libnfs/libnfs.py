# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _libnfs
else:
    import _libnfs

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)



def new_NFSFileHandle():
    return _libnfs.new_NFSFileHandle()

def copy_NFSFileHandle(value):
    return _libnfs.copy_NFSFileHandle(value)

def delete_NFSFileHandle(obj):
    return _libnfs.delete_NFSFileHandle(obj)

def NFSFileHandle_assign(obj, value):
    return _libnfs.NFSFileHandle_assign(obj, value)

def NFSFileHandle_value(obj):
    return _libnfs.NFSFileHandle_value(obj)

def new_uint64_t_ptr():
    return _libnfs.new_uint64_t_ptr()

def copy_uint64_t_ptr(value):
    return _libnfs.copy_uint64_t_ptr(value)

def delete_uint64_t_ptr(obj):
    return _libnfs.delete_uint64_t_ptr(obj)

def uint64_t_ptr_assign(obj, value):
    return _libnfs.uint64_t_ptr_assign(obj, value)

def uint64_t_ptr_value(obj):
    return _libnfs.uint64_t_ptr_value(obj)

def new_NFSDirHandle():
    return _libnfs.new_NFSDirHandle()

def copy_NFSDirHandle(value):
    return _libnfs.copy_NFSDirHandle(value)

def delete_NFSDirHandle(obj):
    return _libnfs.delete_NFSDirHandle(obj)

def NFSDirHandle_assign(obj, value):
    return _libnfs.NFSDirHandle_assign(obj, value)

def NFSDirHandle_value(obj):
    return _libnfs.NFSDirHandle_value(obj)

def new_TimeValArray(nelements):
    return _libnfs.new_TimeValArray(nelements)

def delete_TimeValArray(ary):
    return _libnfs.delete_TimeValArray(ary)

def TimeValArray_getitem(ary, index):
    return _libnfs.TimeValArray_getitem(ary, index)

def TimeValArray_setitem(ary, index, value):
    return _libnfs.TimeValArray_setitem(ary, index, value)
class timeval(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    tv_sec = property(_libnfs.timeval_tv_sec_get, _libnfs.timeval_tv_sec_set)
    tv_usec = property(_libnfs.timeval_tv_usec_get, _libnfs.timeval_tv_usec_set)

    def __init__(self):
        _libnfs.timeval_swiginit(self, _libnfs.new_timeval())
    __swig_destroy__ = _libnfs.delete_timeval

# Register timeval in _libnfs:
_libnfs.timeval_swigregister(timeval)

class nfs_url(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    server = property(_libnfs.nfs_url_server_get, _libnfs.nfs_url_server_set)
    path = property(_libnfs.nfs_url_path_get, _libnfs.nfs_url_path_set)
    file = property(_libnfs.nfs_url_file_get, _libnfs.nfs_url_file_set)

    def __init__(self):
        _libnfs.nfs_url_swiginit(self, _libnfs.new_nfs_url())
    __swig_destroy__ = _libnfs.delete_nfs_url

# Register nfs_url in _libnfs:
_libnfs.nfs_url_swigregister(nfs_url)

class nfs_stat_64(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    nfs_dev = property(_libnfs.nfs_stat_64_nfs_dev_get, _libnfs.nfs_stat_64_nfs_dev_set)
    nfs_ino = property(_libnfs.nfs_stat_64_nfs_ino_get, _libnfs.nfs_stat_64_nfs_ino_set)
    nfs_mode = property(_libnfs.nfs_stat_64_nfs_mode_get, _libnfs.nfs_stat_64_nfs_mode_set)
    nfs_nlink = property(_libnfs.nfs_stat_64_nfs_nlink_get, _libnfs.nfs_stat_64_nfs_nlink_set)
    nfs_uid = property(_libnfs.nfs_stat_64_nfs_uid_get, _libnfs.nfs_stat_64_nfs_uid_set)
    nfs_gid = property(_libnfs.nfs_stat_64_nfs_gid_get, _libnfs.nfs_stat_64_nfs_gid_set)
    nfs_rdev = property(_libnfs.nfs_stat_64_nfs_rdev_get, _libnfs.nfs_stat_64_nfs_rdev_set)
    nfs_size = property(_libnfs.nfs_stat_64_nfs_size_get, _libnfs.nfs_stat_64_nfs_size_set)
    nfs_blksize = property(_libnfs.nfs_stat_64_nfs_blksize_get, _libnfs.nfs_stat_64_nfs_blksize_set)
    nfs_blocks = property(_libnfs.nfs_stat_64_nfs_blocks_get, _libnfs.nfs_stat_64_nfs_blocks_set)
    nfs_atime = property(_libnfs.nfs_stat_64_nfs_atime_get, _libnfs.nfs_stat_64_nfs_atime_set)
    nfs_mtime = property(_libnfs.nfs_stat_64_nfs_mtime_get, _libnfs.nfs_stat_64_nfs_mtime_set)
    nfs_ctime = property(_libnfs.nfs_stat_64_nfs_ctime_get, _libnfs.nfs_stat_64_nfs_ctime_set)
    nfs_atime_nsec = property(_libnfs.nfs_stat_64_nfs_atime_nsec_get, _libnfs.nfs_stat_64_nfs_atime_nsec_set)
    nfs_mtime_nsec = property(_libnfs.nfs_stat_64_nfs_mtime_nsec_get, _libnfs.nfs_stat_64_nfs_mtime_nsec_set)
    nfs_ctime_nsec = property(_libnfs.nfs_stat_64_nfs_ctime_nsec_get, _libnfs.nfs_stat_64_nfs_ctime_nsec_set)
    nfs_used = property(_libnfs.nfs_stat_64_nfs_used_get, _libnfs.nfs_stat_64_nfs_used_set)

    def __init__(self):
        _libnfs.nfs_stat_64_swiginit(self, _libnfs.new_nfs_stat_64())
    __swig_destroy__ = _libnfs.delete_nfs_stat_64

# Register nfs_stat_64 in _libnfs:
_libnfs.nfs_stat_64_swigregister(nfs_stat_64)

class nfsdirent(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    next = property(_libnfs.nfsdirent_next_get, _libnfs.nfsdirent_next_set)
    name = property(_libnfs.nfsdirent_name_get, _libnfs.nfsdirent_name_set)
    inode = property(_libnfs.nfsdirent_inode_get, _libnfs.nfsdirent_inode_set)
    type = property(_libnfs.nfsdirent_type_get, _libnfs.nfsdirent_type_set)
    mode = property(_libnfs.nfsdirent_mode_get, _libnfs.nfsdirent_mode_set)
    size = property(_libnfs.nfsdirent_size_get, _libnfs.nfsdirent_size_set)
    atime = property(_libnfs.nfsdirent_atime_get, _libnfs.nfsdirent_atime_set)
    mtime = property(_libnfs.nfsdirent_mtime_get, _libnfs.nfsdirent_mtime_set)
    ctime = property(_libnfs.nfsdirent_ctime_get, _libnfs.nfsdirent_ctime_set)
    uid = property(_libnfs.nfsdirent_uid_get, _libnfs.nfsdirent_uid_set)
    gid = property(_libnfs.nfsdirent_gid_get, _libnfs.nfsdirent_gid_set)
    nlink = property(_libnfs.nfsdirent_nlink_get, _libnfs.nfsdirent_nlink_set)
    dev = property(_libnfs.nfsdirent_dev_get, _libnfs.nfsdirent_dev_set)
    rdev = property(_libnfs.nfsdirent_rdev_get, _libnfs.nfsdirent_rdev_set)
    blksize = property(_libnfs.nfsdirent_blksize_get, _libnfs.nfsdirent_blksize_set)
    blocks = property(_libnfs.nfsdirent_blocks_get, _libnfs.nfsdirent_blocks_set)
    used = property(_libnfs.nfsdirent_used_get, _libnfs.nfsdirent_used_set)
    atime_nsec = property(_libnfs.nfsdirent_atime_nsec_get, _libnfs.nfsdirent_atime_nsec_set)
    mtime_nsec = property(_libnfs.nfsdirent_mtime_nsec_get, _libnfs.nfsdirent_mtime_nsec_set)
    ctime_nsec = property(_libnfs.nfsdirent_ctime_nsec_get, _libnfs.nfsdirent_ctime_nsec_set)

    def __init__(self):
        _libnfs.nfsdirent_swiginit(self, _libnfs.new_nfsdirent())
    __swig_destroy__ = _libnfs.delete_nfsdirent

# Register nfsdirent in _libnfs:
_libnfs.nfsdirent_swigregister(nfsdirent)

class nfs_server_list(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    next = property(_libnfs.nfs_server_list_next_get, _libnfs.nfs_server_list_next_set)
    addr = property(_libnfs.nfs_server_list_addr_get, _libnfs.nfs_server_list_addr_set)

    def __init__(self):
        _libnfs.nfs_server_list_swiginit(self, _libnfs.new_nfs_server_list())
    __swig_destroy__ = _libnfs.delete_nfs_server_list

# Register nfs_server_list in _libnfs:
_libnfs.nfs_server_list_swigregister(nfs_server_list)


def nfs_init_context():
    return _libnfs.nfs_init_context()

def nfs_destroy_context(nfs):
    return _libnfs.nfs_destroy_context(nfs)

def nfs_get_error(nfs):
    return _libnfs.nfs_get_error(nfs)

def nfs_set_auth(nfs, auth):
    return _libnfs.nfs_set_auth(nfs, auth)

def nfs_parse_url_full(nfs, url):
    return _libnfs.nfs_parse_url_full(nfs, url)

def nfs_parse_url_dir(nfs, url):
    return _libnfs.nfs_parse_url_dir(nfs, url)

def nfs_parse_url_incomplete(nfs, url):
    return _libnfs.nfs_parse_url_incomplete(nfs, url)

def nfs_destroy_url(url):
    return _libnfs.nfs_destroy_url(url)

def nfs_get_readmax(nfs):
    return _libnfs.nfs_get_readmax(nfs)

def nfs_get_writemax(nfs):
    return _libnfs.nfs_get_writemax(nfs)

def nfs_set_tcp_syncnt(nfs, v):
    return _libnfs.nfs_set_tcp_syncnt(nfs, v)

def nfs_set_uid(nfs, uid):
    return _libnfs.nfs_set_uid(nfs, uid)

def nfs_set_gid(nfs, gid):
    return _libnfs.nfs_set_gid(nfs, gid)

def nfs_set_readahead(nfs, v):
    return _libnfs.nfs_set_readahead(nfs, v)

def nfs_mount(nfs, server, exportname):
    return _libnfs.nfs_mount(nfs, server, exportname)

def nfs_stat64(nfs, path, st):
    return _libnfs.nfs_stat64(nfs, path, st)

def nfs_lstat64(nfs, path, st):
    return _libnfs.nfs_lstat64(nfs, path, st)

def nfs_fstat64(nfs, nfsfh, st):
    return _libnfs.nfs_fstat64(nfs, nfsfh, st)

def nfs_open(nfs, path, flags, nfsfh):
    return _libnfs.nfs_open(nfs, path, flags, nfsfh)

def nfs_close(nfs, nfsfh):
    return _libnfs.nfs_close(nfs, nfsfh)

def nfs_pread(nfs, nfsfh, offset, count, buff):
    return _libnfs.nfs_pread(nfs, nfsfh, offset, count, buff)

def nfs_read(nfs, nfsfh, count, buff):
    return _libnfs.nfs_read(nfs, nfsfh, count, buff)

def nfs_pwrite(nfs, nfsfh, offset, count, buff):
    return _libnfs.nfs_pwrite(nfs, nfsfh, offset, count, buff)

def nfs_write(nfs, nfsfh, count, buff):
    return _libnfs.nfs_write(nfs, nfsfh, count, buff)

def nfs_lseek(nfs, nfsfh, offset, whence, current_offset):
    return _libnfs.nfs_lseek(nfs, nfsfh, offset, whence, current_offset)

def nfs_fsync(nfs, nfsfh):
    return _libnfs.nfs_fsync(nfs, nfsfh)

def nfs_truncate(nfs, path, length):
    return _libnfs.nfs_truncate(nfs, path, length)

def nfs_ftruncate(nfs, nfsfh, length):
    return _libnfs.nfs_ftruncate(nfs, nfsfh, length)

def nfs_mkdir(nfs, path):
    return _libnfs.nfs_mkdir(nfs, path)

def nfs_mkdir2(nfs, path, mode):
    return _libnfs.nfs_mkdir2(nfs, path, mode)

def nfs_rmdir(nfs, path):
    return _libnfs.nfs_rmdir(nfs, path)

def nfs_creat(nfs, path, mode, nfsfh):
    return _libnfs.nfs_creat(nfs, path, mode, nfsfh)

def nfs_create(nfs, path, flags, mode, nfsfh):
    return _libnfs.nfs_create(nfs, path, flags, mode, nfsfh)

def nfs_mknod(nfs, path, mode, dev):
    return _libnfs.nfs_mknod(nfs, path, mode, dev)

def nfs_unlink(nfs, path):
    return _libnfs.nfs_unlink(nfs, path)

def nfs_opendir(nfs, path, nfsdir):
    return _libnfs.nfs_opendir(nfs, path, nfsdir)

def nfs_readdir(nfs, nfsdir):
    return _libnfs.nfs_readdir(nfs, nfsdir)

def nfs_closedir(nfs, nfsdir):
    return _libnfs.nfs_closedir(nfs, nfsdir)

def nfs_chdir(nfs, path):
    return _libnfs.nfs_chdir(nfs, path)

def nfs_getcwd(nfs, cwd):
    return _libnfs.nfs_getcwd(nfs, cwd)

def nfs_readlink(nfs, path, buff, bufsize):
    return _libnfs.nfs_readlink(nfs, path, buff, bufsize)

def nfs_readlink2(nfs, path, buf):
    return _libnfs.nfs_readlink2(nfs, path, buf)

def nfs_chmod(nfs, path, mode):
    return _libnfs.nfs_chmod(nfs, path, mode)

def nfs_lchmod(nfs, path, mode):
    return _libnfs.nfs_lchmod(nfs, path, mode)

def nfs_fchmod(nfs, nfsfh, mode):
    return _libnfs.nfs_fchmod(nfs, nfsfh, mode)

def nfs_chown(nfs, path, uid, gid):
    return _libnfs.nfs_chown(nfs, path, uid, gid)

def nfs_lchown(nfs, path, uid, gid):
    return _libnfs.nfs_lchown(nfs, path, uid, gid)

def nfs_fchown(nfs, nfsfh, uid, gid):
    return _libnfs.nfs_fchown(nfs, nfsfh, uid, gid)

def nfs_utimes(nfs, path, times):
    return _libnfs.nfs_utimes(nfs, path, times)

def nfs_lutimes(nfs, path, times):
    return _libnfs.nfs_lutimes(nfs, path, times)

def nfs_utime(nfs, path, times):
    return _libnfs.nfs_utime(nfs, path, times)

def nfs_access(nfs, path, mode):
    return _libnfs.nfs_access(nfs, path, mode)

def nfs_symlink(nfs, oldpath, newpath):
    return _libnfs.nfs_symlink(nfs, oldpath, newpath)

def nfs_rename(nfs, oldpath, newpath):
    return _libnfs.nfs_rename(nfs, oldpath, newpath)

def nfs_link(nfs, oldpath, newpath):
    return _libnfs.nfs_link(nfs, oldpath, newpath)

def mount_getexports(server):
    return _libnfs.mount_getexports(server)

def mount_free_export_list(exports):
    return _libnfs.mount_free_export_list(exports)

def nfs_find_local_servers():
    return _libnfs.nfs_find_local_servers()

def free_nfs_srvr_list(srv):
    return _libnfs.free_nfs_srvr_list(srv)

def nfs_set_timeout(nfs, milliseconds):
    return _libnfs.nfs_set_timeout(nfs, milliseconds)

def nfs_get_timeout(nfs):
    return _libnfs.nfs_get_timeout(nfs)


