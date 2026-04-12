import arrow

brewing_time = arrow.utcnow();
brewing_time = brewing_time.to("Europe/Rome");

print(f"Europe Rome time: {brewing_time}")

from collections import namedtuple

chai_Profile = namedtuple("chai_Profile",["flavour","aroma"])
print(f"chai_profile: {chai_Profile}")