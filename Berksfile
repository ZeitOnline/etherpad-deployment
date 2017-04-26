# -*- ruby -*-

# Zeit Online cookbooks
STYX = "git@styx2.zeit.de:/home/git/chef.git"
{
  "zeit-sso" => "32b752e",  # 1.1.0
  "zeit-batou-target" => "a94506a",  # 0.1.11
}.each do |name, commit|
  cookbook(
    name, ref: commit,
    git: STYX, branch: "chefServer", rel: "cookbooks/#{name}")
end

# 3rdparty cookbooks
source "https://supermarket.chef.io"

cookbook "nginx", "=2.7.4"
  cookbook "apt", "=2.9.2"
  cookbook "bluepill", "=2.3.1"
    cookbook "rsyslog", "=1.12.2"
  cookbook "build-essential", "=2.0.4"
  cookbook "ohai", "=2.0.1"
  cookbook "runit", "=1.5.10"
    cookbook "yum", "=3.8.1"
    cookbook "yum-epel", "=0.3.6"

cookbook "nodejs", "=2.4.0"
  # apt
  # build-essential
  # yum-epel
  cookbook "ark", "=0.9.0"
    # build-essential
    cookbook "windows", "=2.0.2"
    cookbook "seven_zip", "=2.0.2"
  cookbook "homebrew", "=1.7.2"

cookbook "database", "=2.3.0"
  cookbook "aws", "=2.5.0"
  cookbook "postgresql", "=3.4.12"
    # apt
    # build-essential
    cookbook "openssl", "=2.0.2"
      cookbook "chef-sugar", "=3.1.1"
  cookbook "mysql", "=5.6.1"
    cookbook "yum-mysql-community", "=0.1.10"
      cookbook "compat_resource", "=12.7.3"
  cookbook "mysql-chef_gem", "=0.0.5"
  cookbook "xfs", "=1.1.0"
