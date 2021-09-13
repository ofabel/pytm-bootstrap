from base64 import b64decode
from base64 import b64encode
from hmac import compare_digest
from hmac import digest
from pickle import dumps
from pickle import loads


class Serializer:
    HMAC_DIGEST: str = 'sha512'

    def __init__(self, secret: str):
        self._secret: bytes = bytes(secret, 'utf-8')

    def serialize(self, data: dict) -> (str, str):
        data_dump: bytes = dumps(data)
        data_b64: bytes = b64encode(data_dump)
        signature: bytes = self._sign_data(data_b64)

        return signature.decode('utf-8'), data_b64.decode('utf-8')

    def deserialize(self, signature: str, data: str) -> dict:
        data_decoded: bytes = b64decode(data, None, True)
        signature_as_bytes: bytes = bytes(signature, 'utf-8')

        if not self._check_signature(signature_as_bytes, data_decoded):
            raise RuntimeError('signature does not match')

        return loads(data_decoded)

    def _sign_data(self, data: bytes) -> bytes:
        signature: bytes = digest(self._secret, data, Serializer.HMAC_DIGEST)

        return b64encode(signature)

    def _check_signature(self, signature: bytes, data: bytes) -> bool:
        signature_to_compare: bytes = self._sign_data(data)
        decoded_signature: bytes = b64decode(signature)

        return compare_digest(decoded_signature, signature_to_compare)
