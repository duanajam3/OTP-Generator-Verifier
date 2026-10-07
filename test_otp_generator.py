import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import otp_generator as otp

secret = "demo-secret"

original_time = otp.time.time
otp.time.time = lambda: 1700000000

generated = otp.generate_event_otp(secret)
assert len(generated) == 6
assert generated.isdigit()

assert otp.verify_event_otp(secret, generated, validity_window=0)

assert not otp.verify_event_otp(secret, "000000", validity_window=0)

otp.time.time = original_time

print("All OTP tests passed.")
