import collectd

PATH = '/proc/sys/fs/file-nr'

def read(data=None):
    with open(PATH,'r') as f:
        open_fd = f.read().split()[0]

    collectd.Values(
        plugin='open_files', type='gauge', type_instance='fd'
    ).dispatch(
        values=[open_fd]
    )

collectd.register_read(read
