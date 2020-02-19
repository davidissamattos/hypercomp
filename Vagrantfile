# encoding: utf-8
# -*- mode: ruby -*-
# vi: set ft=ruby :
# Box / OS
VAGRANT_BOX = 'ubuntu/bionic64'
VM_NAME = 'hypercomp'
VM_USER = 'vagrant'

MAC_USER = 'davidis'
HOST_PATH = '.'

GUEST_PATH = '/home/' + VM_USER + '/' + VM_NAME
Vagrant.configure(2) do |config|
  config.vm.box = VAGRANT_BOX
  config.vm.hostname = VM_NAME
  config.vm.provider "virtualbox" do |v|
    v.name = VM_NAME
    v.memory = 2048
  end
  #DHCP — comment this out if planning on using NAT instead
  config.vm.network "private_network", type: "dhcp"
  # # Port forwarding — uncomment this to use NAT instead of DHCP
  # config.vm.network "forwarded_port", guest: 80, host: VM_PORT

  # Sync folder
  config.vm.synced_folder HOST_PATH, GUEST_PATH
  # Disable default Vagrant folder, use a unique path per project
  config.vm.synced_folder '.', '/home/'+VM_USER+'', disabled: true
  # Setup
  config.vm.provision "shell",
    path: "setup.sh",
    args: GUEST_PATH
end