def test_sign_jld(jld_document, private_key, expected_jld_document_signed):
    from jld_signatures import sign

    signed_jld_document = sign(jld_document, private_key)
    # pop the created time key since its dynamic
    signed_jld_document['signature'].pop('created')

    assert signed_jld_document == expected_jld_document_signed


def test_verify_jld(expected_jld_document_signed, private_key):
    from jld_signatures import verify

    assert verify(expected_jld_document_signed, private_key) is True
