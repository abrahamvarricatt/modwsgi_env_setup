# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  
  config.vm.box = "bento/centos-6.7"
  config.vm.box_check_update = false
  config.ssh.forward_agent = true

  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
    v.cpus = 1
    v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
  end

  config.vm.define "bottle" do |bottle|
    bottle.vm.hostname = "bottle"
    bottle.vm.network "private_network", ip: "192.168.33.10"
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provision/site.yml"
    ansible.inventory_path = "provision/hosts/vagrant"
    ansible.limit = "all"
    # ansible.verbose = "vvvv"
  end

end
