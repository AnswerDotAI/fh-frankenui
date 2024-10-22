
# https://github.com/cloudflare/cloudflare-python/blob/main/api.md
from fastcore.script import *
from cloudflare import Cloudflare

@call_parse
def add_dns_record(
    record_type: str,  # Type of DNS record (CNAME or A)
    target: str,       # Target IP address or domain name
    record: str,       # Record name (without the zone)
    zone: str,         # Zone name
    proxied: bool_arg=True # Use CF proxy?
):
    cf = Cloudflare()
    zones = cf.zones.list(name=zone)
    if not zones: raise ValueError(f"Zone '{zone}' not found")
    zid = zones.result[0].id
    cf.dns.records.create(zone_id=zid, type=record_type.upper(), name=f"{record}.{zone}", content=target, proxied=proxied)
