+ step 1: create the mount point

```sh
sudo mkdir /run/media/zds/Study
sudo mkdir /run/media/zds/Download
```

+ step 2: find the UUID, disk name of certain disks

```sh
lsblk
blkid
```

+ step 3: edit the /etc/fstab

```sh
# for example
UUID=7E24E44524E4024F /run/media/zds/Study ntfs defaults 0 2
UUID=7EC6A56DC6A5267D /run/media/zds/Download ntfs defaults 0 2
# test
sudo mount -a
```
