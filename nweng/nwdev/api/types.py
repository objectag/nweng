import re
import socket

class TagProcessor:
    def __init__(self):
        self.type_validators = {
            'string': self.validate_string,
            'email': self.validate_email,
            'ipv4': self.validate_ipv4,
            'ipv6': self.validate_ipv6,
            'interface': self.validate_interface,
            'sid': self.validate_sid
        }

    def validate_string(self, tag_value):
        return str(tag_value)

    def validate_email(self, tag_value):
        try:
            if re.match(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$', tag_value):
                return tag_value
            else:
                return '<<InvalidEmail>>'
        except (TypeError):
            return '<<InvalidEmail>>'

    def validate_ipv4(self, tag_value):
        def is_valid_ipv4(ip_address):
            try:
                socket.inet_pton(socket.AF_INET, ip_address)
                return True
            except (TypeError, ValueError, socket.error):
                return False

        def is_valid_ipv4_with_prefix(ip_with_prefix):
            try:
                ip, prefix = ip_with_prefix.split('/')
                if 0 <= int(prefix) <= 32:
                    return is_valid_ipv4(ip)
            except (AttributeError, TypeError, ValueError, socket.error):
                pass
            return False
      
        if is_valid_ipv4(tag_value) or is_valid_ipv4_with_prefix(tag_value):
            return tag_value
        else:
            return '<<InvalidIPv4>>' 

    def validate_ipv6(self, tag_value):
        def is_valid_ipv6(ip_address):
            try:
                socket.inet_pton(socket.AF_INET6, ip_address)
                return True
            except (TypeError, ValueError, socket.error):
                return False
        
        def is_valid_ipv6_with_prefix(ip_with_prefix):
            try:
                ip, prefix_length = ip_with_prefix.split("/")
                socket.inet_pton(socket.AF_INET6, ip)
                if 0 <= int(prefix_length) <= 128:
                    return True
                else:
                    return False
            except (AttributeError, TypeError, ValueError, socket.error):
                return False
      
        if is_valid_ipv6(tag_value) or is_valid_ipv6_with_prefix(tag_value):
            return tag_value
        else:
            return '<<InvalidIPv6>>' 

    def validate_interface(self, tag_value):
        try:
            if not re.match("^(lo0|ae[0-9]{1,2}|[g|x]e-[0-9]{1}\/[0-9]{1}\/[0-9]{1,2})((\.0{1})*|\.[1-9]{1}[0-9]{0,2}|\.[1-3]{1}[0-9]{3}|\.4{1}0{1}[0-9]{1}[0-5]{1})$", tag_value):
                #msg = "invalid input: " + tag_value + " - valid: lo.[0-4095], ae*.[0-4095], 0-ge-*/*/*.[0-4095] or xe-*/*/*.[0-4095]"
                return '<<InvalidInterface>>'
            return tag_value
        except:
            return '<<InvalidEmail>>'


    def validate_sid(self, tag_value):
        if not re.match("^^([a-f]|[0-9]){8}$", tag_value):
            msg = "invalid input: " + id + " - valid: 8 hexadecimal digits"
            return '<<InvalidSID>>'
        return tag_value

    def check_tag_value(self, tag_type, tag_value):
        validator_func = self.type_validators.get(tag_type, self.unknown_type_validator)
        return validator_func(tag_value)

    def unknown_type_validator(self, tag_value):
        return '<<UnknownType>>'


