def test_sign_jws(private_key, expected_jws_signature):
    from jws import sign_jws

    payload = b'$.02'
    jws_signature = sign_jws(payload, private_key)

    assert jws_signature == expected_jws_signature


def test_verify_jws(private_key, public_key, expected_jws_signature):
    from jws import verify_jws

    payload = b'$.02'
    assert verify_jws(payload, expected_jws_signature, public_key) is True
