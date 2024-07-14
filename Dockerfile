FROM opensuse/tumbleweed:latest

# Install dependencies and setup environment
RUN zypper refresh && zypper update -y
RUN zypper install -y git osc