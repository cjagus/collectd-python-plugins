# collectd-python-plugins
Usefull collectd plugins

* open_files.py ( Monitor File descriptor usage in Linux)
* aws_spotinstance_monitor.py ( Monitor spot termination based on az, instane type and class)

# Configuration

Enable the python plugin and place the python scrips in `/opt/collectd`

```
LoadPlugin python
<Plugin python>
    ModulePath "/opt/collectd_plugins"
    Import "cpu_temp"
    <Module cpu_temp>
        Path "/sys/class/thermal/thermal_zone0/temp"
    </Module>
</Plugin>
```
# Notes 
When using with graphite set `EscapeCharacter "."` in `Plugin write_graphite` config
