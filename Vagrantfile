# -*- mode: ruby -*-

Vagrant.configure("2") do |config|
  config.vm.box_check_update = false

  config.berkshelf.enabled = true
  config.ssh.forward_agent = true

  if RUBY_PLATFORM =~ /darwin/ then
    config.vm.provider "virtualbox" do |vb|
      vb.memory = 1024
      # https://github.com/mitchellh/vagrant/issues/1807
      vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
      # https://superuser.com/a/850389
      vb.customize ["modifyvm", :id, "--nictype1", "virtio" ]
    end
    config.vm.box = "ubuntu/trusty64"
  else
    config.vm.provider "lxc"
    config.vm.box = "fgrehm/trusty64-lxc"
  end

  config.vm.define "etherpad" do |node|
    node.vm.hostname = "etherpad"

    node.vm.network "forwarded_port", guest: 80, host: 8080

    chef_solo(node) do |chef|
      chef.add_recipe "recipe[nginx]"
      chef.add_recipe "recipe[zeit-batou-target]"
      chef.add_recipe "recipe[zeit-batou-target::nginx]"
      chef.add_recipe "recipe[nodejs]"
      chef.add_recipe "recipe[zeit-sso::postgresql-server]"

      chef.json = {
        "postgresql" => {
          "enable_pgdg_apt" => true,
          "version" => "9.6",
          "password" => {
            "postgres" => "postgres",
          },
          "database" => {
            "name" => "etherpad",
            "user" => "etherpad",
            "password" => "etherpad",
          }
        },
        "nginx" => {
          "default_site_enabled" => false,
        },
        "batou" => {
          "deploymentUsers" => ["vagrant"],
          "nginx_config" => "/home/vagrant/deployment/work/nginx/etherpad.conf",
        },
      }
    end
  end

end


def chef_solo(node)
  node.vm.provision "shell", inline: "if [ ! -x /opt/chef/bin/chef-solo ]; then echo 'Downloading chef'; wget -q https://opscode-omnibus-packages.s3.amazonaws.com/debian/6/x86_64/chef_12.2.1-1_amd64.deb && dpkg -i chef_12.2.1-1_amd64.deb ; else echo 'chef already installed'; fi"
  node.vm.provision "chef_solo" do |chef|
    chef.install = false
    chef.log_level = ENV.fetch("CHEF_LOG", "info").downcase.to_sym
    chef.add_recipe "recipe[apt]"  # in case the vagrant box is a bit stale
    yield chef
  end
end
