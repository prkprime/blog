# Introduction to NixOS 

I have been using Linux as my daily driver on and off for the past few years. Arch Linux and Ubuntu were always the distribution of choice. I used Arch Linux because I liked the rolling release nature and it allowed me to do a lot of things I might not have been able to do easily on Ubuntu. Like using efistub instead of a bootloader and using f2fs filesystem for my root partition. But whenever I was being lazy or needed to introduce my friend to Linux, I would install Ubuntu and debloat it enough to my liking.  

However, I had my fair share of issues with both. Every time I did a system upgrade on Arch, I knew there was a slight chance that something is going to break, and I would have to waste my time fixing. (Not that I am blaming arch, that is just the nature of rolling release). My issues on Ubuntu were due to the lack of bleeding edge packages in repository, abandoned PPAs, nothing like AUR and the list goes on. 

Once I was bitching about how no distro works good and how native Windows with WSL2 works simply fine, I was suggested NixOS. NixOS is a Linux distribution which follows the rolling release pattern but has a unique package management and system configuration. Being the distro-hopper I am, I wiped my Windows and installed NixOS. In this blog, I will guide you through my journey using NixOS 

# Installing NixOS 

So I went to the NixOS download page. I downloaded the latest unstable live ISO (nixos-20.09 at the time of writing). Flashed it on my pen drive and booted it. The live environment was using Plasma 5.18 and it had a `configuration.nix` using plasma accordingly. 

I partitioned my disk and formatted it accordingly with root, home, swap, and boot and mounted them at /mnt. Now this is where things got interesting. I opened the NixOS installation part from the wiki here. And I realised that even though it is a Graphical Live ISO, it doesn’t have a graphical installer, and it does not use your standard package manager. Like apt, dnf and pacman sure have different syntaxes but they function predictably. You must generate a sample config by using 

```# nixos-generate-config --root /mnt 

``` 

You should not touch the hardware-config. So, all you have to edit is the `configuration.nix` located in 

```# nano /mnt/etc/nixos/configuration.nix 

``` 
Here is a [link](https://del.dog/gotenksnixos) to what I use (I will be updating it as I modify it). 

Once you are done with the config, enter 

```# nixos-install 

``` 
to start the installation. You can use nixos-enter to chroot into the system to set the password to the user you created in the configuration. Reboot once you are done. If all goes well, you will be booted in NixOS. 

# Setting up and customizing NixOS 

So, the first thing I always do upon booting the distro for the first time is setting up the terminal themes, zsh and its plugins. I went on searching for the syntax for the nix package manager. I found this handy-dandy cheat sheet on the nixos website. I installed zsh, git and all the other relevant things. That’s when I stumbled onto my first roadblock, chsh doesn’t work. Because there is no `/usr/bin/zsh`. You have to set the default shell in `configuration.nix`. Add 

``` 

{ pkgs, ... }: 

{
  ...
  users.users.<myusername> = {
    ...
    shell = pkgs.zsh;
    ...
  };
}
``` 

to your user in the `configuration.nix`. Every time you want to update your system after changing `configuration.nix`, run 

```# nixos-rebuild <switch/boot> 

``` 

,where switch will change it instantly while boot will set it as next boot. I felt the boot time a bit too slow in the beginning, hence, I switched from dhcpcd and GDDM to Network-Manager and LightDM respectively. You can refer to the config I shared above in the installation section to know what I did change in `configuration.nix`. Afterwards I switched to the latest testing kernel by adding 

```boot.kernelPackages = pkgs.linuxPackages_testing; 

``` 

to the `configuration.nix`. I then had to allow using unfree packages to use packages like VSCode. To do that add  

```nixpkgs.config.allowUnfree = true; 

``` 

to the `configuration.nix`. And this I completed my initial setup. 

# My thoughts on the experience 

Overall, I really liked using NixOS. The features I loved about NixOS are 

## Atomic Upgrades/Rollbacks 

NixOS has a transactional approach to configuration management: configuration changes such as upgrades are atomic. This means that if the upgrade to a new configuration is interrupted — say, the power fails half-way through — the system will still be in a consistent state: it will either boot in the old or the new configuration. In most other systems, you’ll end up in an inconsistent state, and your machine may not even boot anymore. Because the files of a new configuration don’t overwrite old ones, you can (atomically) roll back to a previous configuration. For instance, if after a `nixos-rebuild switch` you discover that you don’t like the new configuration, you can just go back: using `nixos-rebuild switch –rollback` 

## Safe to test changes 

NixOS makes it safe to test your configuration after changing something potentially dangerous. Just use `nixos-rebuild test`, this will build and activate the new configuration but doesn’t make it boot default. Thus, rebooting the system will take you back to the previous well-known good configuration. 

## Consistency 

The Nix package manager ensures that the running system is ‘consistent’ with the logical specification of the system, meaning that it will rebuild all packages that need to be rebuilt. For instance, if you change the kernel, Nix will ensure that external kernel modules such as the NVIDIA driver will be rebuilt as well — so you never run into an X server that mysteriously fails to start after a kernel security upgrade. And if you update the OpenSSL library, Nix ensures that all packages in the system use the new version, even packages that statically link against OpenSSL. 

## Declarative system configuration model 

In NixOS, the entire operating system — the kernel, applications, system packages, configuration files, and so on — is built by the Nix package manager from a description in a purely functional build language. The fact that it’s purely functional essentially means that building a new configuration cannot overwrite previous configurations. Most of the other features follow from this. 

You configure a NixOS system by writing a specification of the functionality that you want on your machine in `/etc/nixos/configuration.nix`. 

Overall, I would recommend this over any other distro I have used because of the reasons I have mentioned above. However, it’s not all rainbows and sunshine. Since it uses an entirely different package system, you might run into issues when programs use hardcoded symlinks to the binaries or something other. Just make sure once that the packages you use work well with NixOS. Luckily, the community is very welcoming and not at all toxic. I am sure that these problems will be gone as the system and community matures. 

Here’s an excerpt from the [note](https://github.com/msfjarvis/dotfiles/blob/master/nixos/NOTES.md) my friend [Harsh](https://github.com/msfjarvis) wrote for nixos. It has some things you might need if you run into issues on NixOS. 

``` Using NixOS is not straightforward, or simple. It's an ordeal to say the least, and a massive pain in the ass if we're being frank. But it's premise is very interesting, so we shall put up with this atrocity for the sake of science and sanity. 

```
I had to patch the nvidia driver just to be able to use the latest rc kernel and Harsh had to upstream the wifi driver for it to work. Doing that wasn't that hard, you can check [my repo](https://github.com/gotenksIN/nixpkgs). If you don't have the time and energy to do potentially something like this, NixOS isn't for you. But if you do, this might be the best istro you ever used.