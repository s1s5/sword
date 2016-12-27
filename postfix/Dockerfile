FROM ubuntu:16.04
ENV LANG ja_JP.utf8
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get install -y locales language-pack-ja && \
    dpkg-reconfigure -f noninteractive locales && \
    update-locale LANG=${LANG} && \
    apt-get install -y postfix && \
    apt-get install -y sasl2-bin && \
    apt-get install -y mailutils && \
    apt-get install -y python && \
    apt-get install -y syslog-ng && \
    apt-get upgrade -y && \
    apt-get clean && \
    rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

# Add syslog-ng into runit ADD     build/runit/syslog-ng /etc/service/syslog-ng/run
# Replace the system() source because inside Docker we can't access /proc/kmsg.
# https://groups.google.com/forum/#!topic/docker-user/446yoB0Vx6w
RUN sed -i -E 's/^(\s*)system\(\);/\1unix-stream("\/dev\/log");/' /etc/syslog-ng/syslog-ng.conf

# Uncomment 'SYSLOGNG_OPTS="--no-caps"' to avoid the following warning:
# syslog-ng: Error setting capabilities, capability management disabled; error='Operation not permitted'
# http://serverfault.com/questions/524518/error-setting-capabilities-capability-management-disabled#
RUN sed -i 's/^#\(SYSLOGNG_OPTS="--no-caps"\)/\1/g' /etc/default/syslog-ng
ADD setup.py /setup.py
CMD ["sh", "-c", "service syslog-ng start ; service postfix start ; touch /var/log/mail.log; tail -F /var/log/mail.log"]
