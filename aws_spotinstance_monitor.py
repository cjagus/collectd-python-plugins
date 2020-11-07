import urllib2, subprocess, collectd

NOTICE_URL = "http://169.254.169.254/latest/meta-data/spot/termination-time"

try:
    contents = urllib2.urlopen(NOTICE_URL)
except urllib2.HTTPError, e:
    status = e.code
else:
    status = contents.code

az = subprocess.check_output(["/usr/bin/ec2metadata", "--availability-zone"]).strip()
instance_type = subprocess.check_output(["/usr/bin/ec2metadata", "--instance-type"]).strip()

def read(data=None):

    if status == 200:
        termination_notice = 1
    else:
        termination_notice = 0

    collectd.Values(
        plugin='aws_spot.' + az + '.' + instance_type, type='gauge', type_instance='status'
    ).dispatch(
        values=[spot_termination]
    )

collectd.register_read(read)
