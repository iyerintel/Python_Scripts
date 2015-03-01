from snmp_helper import snmp_get_oid,snmp_extract
from email.mime.text import MIMEText
import smtplib
import cPickle as pickle

def send_mail(recipient, subject, message, sender):
    '''
    Simple function to help simplify sending SMTP email

    Assumes a mailserver is available on localhost
    '''

    message = MIMEText(message)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = recipient

    # Create SMTP connection object to localhost
    smtp_conn = smtplib.SMTP('localhost')

    # Send the email
    smtp_conn.sendmail(sender, recipient, message.as_string())

    # Close SMTP connection

    smtp_conn.quit()

    return True

def obtain_saved_objects(file_name):
    '''
    Read in previously saved running configuration from a pickle file
    Returns a dict:
    {
      'device_name': device_object,
      'device_name': device_object,
    }

      '''

    f = open(file_name, 'r')
    net_devices = {}
    try:
        net_devices = pickle.load(f)
    except EOFError:
        return net_devices

    return net_devices

def main():
    RTR2_IP = '50.242.94.227' #Router IP
    RTR_SNMP = '8061' # SNMP Port number
    COMMUNITY_STRING = 'galileo'

    OID_RUN_LAST_CHANGED = '1.3.6.1.4.1.9.9.43.1.1.1.0'
    SYS_NAME = '1.3.6.1.2.1.1.5.0'

    a_user = 'pysnmp'
    auth_key = 'xxxxx'
    encrypt_key = 'xxxxx'
    snmp_user = (a_user, auth_key, encrypt_key)

    r2 = (RTR2_IP, COMMUNITY_STRING, RTR_SNMP)

    data = {}
    data = obtain_saved_objects('temp.txt')


    run_last_changed_raw = snmp_get_oid(r2, oid=OID_RUN_LAST_CHANGED)
    run_last_changed = int(snmp_extract(run_last_changed_raw))

    snmp_data = snmp_get_oid_v3(r2, snmp_user, oid=SYS_NAME)
    device_name = snmp_extract(snmp_data)

    if data.keys():
        for k, v in data.items():
            rlc = v[0]

        if(run_last_changed > rlc): #compare stored data in temp.txt with extracted current data
            send_mail( 'deepak7ravi@gmail.com', 'change has been made', 'EMERGENCY', 'loudekey@loud.com')

    else:
        data[device_name] = run_last_changed

if __name__ == '__main__':

    main()

                                                                                   