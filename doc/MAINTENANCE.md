## Allow yunohost upgrades

Yeah, it's a crappy workaround, but yunohost conflicts with bind9 so you need some manual stuff
otherwise apt will remove bind9.

When a yunohost upgrade is available:

* Rename `Package: bind9` in /var/lib/dpkg/status
* Run apt upgrade
* Remove the conflict of Yunohost to bind9
* Rename bind9 to its original name

## Compress bind9 logs

`bind9` nsupdate logs can become huge. Execute this command to compress the logs:

```sh
find /var/log/named -regex '\./nsupdate\.log\.[0-9]*' -exec zstd --rm '{}' \;
```
