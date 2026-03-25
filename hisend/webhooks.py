"""
Hisend Webhook signature verification helper.

Usage::

    from hisend.webhooks import verify_webhook

    # In your FastAPI / Flask / Django route:
    body   = request.get_data()           # raw bytes
    sig    = request.headers.get("X-Hisend-Signature", "")
    secret = os.environ["HISEND_WEBHOOK_SECRET"]

    if not verify_webhook(body, sig, secret):
        abort(401, "Invalid webhook signature")

    event = request.get_json()
    # ... handle event
"""

import hashlib
import hmac


def verify_webhook(payload: bytes, signature: str, secret: str) -> bool:
    """Verify the HMAC-SHA256 signature of an incoming Hisend webhook.

    Args:
        payload:   The raw request body bytes exactly as received.
        signature: The value of the ``X-Hisend-Signature`` request header.
        secret:    Your Webhook Signing Secret (starts with ``whsec_``).

    Returns:
        ``True`` if the signature is valid, ``False`` otherwise.
    """
    if not payload or not signature or not secret:
        return False

    expected = hmac.new(
        secret.encode("utf-8"),
        payload,
        hashlib.sha256,
    ).hexdigest()

    return hmac.compare_digest(signature, expected)
