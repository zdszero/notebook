# 开机检测程序

## BIOS

BIOS是被写入CMOS的一段程序，BIOS是开机后计算机启动的第一个程序，BIOS会分析电脑中有
哪些磁盘，并且根据使用者的设定去读取某个磁盘中的MBR的启动代码，然后BIOS的功能就完成
了。

开机流程到操作系统之前
+ BIOS：开机检测程序，开机后执行的第一个软件
+ MBR：开机后访问的第一个分区，其中包含开机管理程序
+ 开机管理程序(boot loader)：一支可读取系统核心文件的软件
+ 核心文件：开始操作系统的功能

## UEFI(unified extensible firmware interface)

BIOS不认识GPT，还得GPT通过兼容模式才可以一起工作，而且BIOS为16位程序，与当今操作系统接轨的功能比较弱。
因此就有了UEFI这个韧体的诞生。

+ UEFI和EFI的区别

UEFI在EFI的基础上发展得到，UEFI具有更加完善的图形驱动功能，并且添加了secure boot功能。

## 对比

| 特性         | BIOS         | UEFI               |
| :-:          | :-:          | :-:                |
| 工作模式     | 16位实模式   | 32位或64位保护模式 |
| 编写语言     | 16位汇编语言 | C语言              |
| 硬件访问机制 | 中断         | 轮询               |

# partition table

## MBR(master boot record)

MBR是计算机开机后访问的第一个扇区，其LBA = (cylinder, head, sector) = (0, 0, 1)，
MBR存放在磁盘的第一个sector，这个扇区（旧磁盘）一般是512B，通常包含如下数据：

+ 开机管理程序(boot loader)，446B

硬盘引导程序的主要作用是检查分区表是否正确并且在系统硬件完成自检以后将控制权交给硬盘上的引导程序（如GNU
GRUB）。它不依赖任何操作系统，而且启动代码也是可以改变的，从而能够实现多系统引导。

boot loader只有446B，是一个非常简洁优美的程序，boot loader包含如下功能：
1. 提供选单：用户可以选择不同的开机项目
2. 载入核心文件：从操作系统启动区段读取代码
3. 转交其他loader：boot loader除了可以安装在MBR之外，还可以安装在每个分区槽的boot sector内，
当前boot loader可以将控制权移交给其他boot loader，因为boot loader只认识自己分区槽中的核心文件，
如果想从其他分区槽中启动核心文件，就必须将控制权移交给所在分区槽boot sector内的boot loader

+ 分区表，64B
+ 结束标志字，4B

第一个分区是磁盘中最重要的分区，如果第一个分区的数据出错，那么磁盘也就基本费了。
当系统向磁盘中写入内容时，必须要参考分区表。

分区的单位一般是磁道cylinder。64B的分区表仅能写入四组分区信息，这四组分区
被称为主分区(primary partition)或者延伸分区(extended partition)。
当分区数量超过4个时，必须使用逻辑分区(logical partition)

MBR分区表的局限性在于其支持的最大卷为2TB，不能满足当今一些磁盘的需求。

> LBA address (logical block address)
> 逻辑区块地址，用逻辑地址代替磁盘访问时的一维线性地址，单位为512B,
> 可以兼容512B和4KB单位的磁盘块。

## GPT(GUID partition table)

GPT使用34个LBA区块来区分分区信息，同时用磁盘最后33个LBA区块来进行备份，GPT没有主、
延伸、逻辑分区的概念，任何分区都可以被视为主分区，都可以用来被格式化。是否支持读取
GPT与开机检测程序有关。

GPT的LBA0用于与MBR兼容。
