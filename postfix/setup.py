# coding: utf-8
import os
import stat
import subprocess


def delete_lines_with_sed(path, sed_pattern, use_sudo=False):
    def escape(value):
        return value.replace('/', '\\/')

    subprocess.check_call(
        ['sed', '-i', "/{}/d".format(escape(sed_pattern)), path])


def append(filename, line):
    with open(filename, 'a') as fp:
        print >> fp, line


def main(relayhost, port, user, password):
    m = {
        'relayhost': '[{}]:{}'.format(relayhost, port),
        'smtp_use_tls': 'yes',
        'smtp_sasl_auth_enable': 'yes',
        'smtp_sasl_password_maps': 'hash:/etc/postfix/sasl_passwd',
        'smtp_sasl_tls_security_options': 'noanonymous',
        'smtp_sasl_mechanism_filter': 'plain',
        'smtp_tls_CApath': '/etc/pki/tls/certs/ca-bundle.crt',
        'smtp_sasl_security_options': 'noanonymous',
        'inet_interfaces': 'loopback-only',
        'smtpd_client_connection_rate_limit': '50',
        # http://www.unix-power.net/linux/centos_postfix.html
        'anvil_rate_time_unit': '900s',
        'smtpd_soft_error_limit': '10',
        'smtpd_hard_error_limit': '30',
        'smtpd_error_sleep_time': '60s',
        'smtpd_client_message_rate_limit': '100',
        'smtpd_client_recipient_rate_limit': '200',
    }
    sasl_passwd = '[{}]:{} {}:{}'.format(
        relayhost, port, user, password)
    main_cf = '/etc/postfix/main.cf'
    for key, value in m.items():
        delete_lines_with_sed(
            main_cf, '{}'.format(key))
        append(main_cf, '{} = {}'.format(key, value))

    sasl_passwd_path = '/etc/postfix/sasl_passwd'
    with open(sasl_passwd_path, 'w') as fp:
        print >> fp, sasl_passwd
    os.chmod(sasl_passwd_path, stat.S_IRUSR | stat.S_IWUSR)
    subprocess.check_call(['postmap', '/etc/postfix/sasl_passwd'])
    subprocess.check_call(['chown', 'root:root', '/etc/postfix/sasl_passwd.db'])
    subprocess.check_call(['chmod', '600', '/etc/postfix/sasl_passwd.db'])
    subprocess.check_call(['/etc/init.d/postfix', 'reload'])


def __entry_point():
    import argparse
    parser = argparse.ArgumentParser(
        description=u'',  # プログラムの説明
    )
    parser.add_argument("args", nargs="*")
    main(*parser.parse_args().args)

if __name__ == '__main__':
    __entry_point()
