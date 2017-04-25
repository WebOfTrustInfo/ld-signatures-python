import pytest


@pytest.fixture
def private_key():
    return (
        '-----BEGIN RSA PRIVATE KEY-----\r\n'
        'MIIEogIBAAKCAQEAtpS1ZmfVKVP5KofIhMBP0tSWc4qlh6fm2lrZSkuKxUjEaWjz\r\n'
        'ZSzs72gEIGxraWusMdoRuV54xsWRyf5KeZT0S+I5Prle3Idi3gICiO4NwvMk6JwS\r\n'
        'BcJWwmSLFEKyUSnB2CtfiGc0/5rQCpcEt/Dn5iM+BNn7fqpoLIbks8rXKUIj8+qM\r\n'
        'VqkTXsEKeKinE23t1ykMldsNaaOH+hvGti5Jt2DMnH1JjoXdDXfxvSP/0gjUYb0e\r\n'
        'ktudYFXoA6wekmQyJeImvgx4Myz1I4iHtkY/Cp7J4Mn1ejZ6HNmyvoTE/4OuY1uC\r\n'
        'eYv4UyXFc1s1uUyYtj4z57qsHGsS4dQ3A2MJswIDAQABAoIBACqdCrmcAmRi9QS4\r\n'
        'LFTPjdHnTDYrZfcDeR39ljmA6CKjmTQBCs3SbnpyDISEyY0RVF9ORlS9d/Lsqdo7\r\n'
        'P6ag3WPYqQO6wCk4cBrg3TaYWR3nIfYodwxhD17PmKZh6ryGwndxqBpt/DCsMWJH\r\n'
        'XRKRZ46PKyp2tfwaSbYaxcYw0YcPQ8SQcnDnR9slk8qetmRDT753iuNB9mue1uEE\r\n'
        'nE4H3nGag+fZtnxlGlml+blJiMWhJrRqCZ3fUROKMsCoYDe/0yu8F0ZagOFKET4h\r\n'
        '9gAq3VPv3C0C/SXNLtBqmSSt9Sw2znjfeUILUgnO9pN1bc8twq1aaeUwAOu7NRo/\r\n'
        'UpJ/ggECgYEA5BGU1c7af/5sFyfsa+onIJgo5BZu8uHvz3Uyb8OA0a+G9UPO1ShL\r\n'
        'YjX0wUfhZcFB7fwPtgmmYAN6wKGVce9eMAbX4PliPk3r+BcpZuPKkuLk/wFvgWAQ\r\n'
        '5Hqw2iEuwXLV0/e8c2gaUt/hyMC5+nFc4v0Bmv6NT6Pfry+UrK3BKWcCgYEAzPD+\r\n'
        'B+nrngwF+O99BHvb47XGKR7ON8JCI6JxavzIkusMXCB8rMyYW8zLs68L8JLAzWZ3\r\n'
        '4oMq0FPUnysBxc5nTF8Nb4BZxTZ5+9cHfoKrYTI3YWsmVW2FpCJFEjMs4NXZ28PB\r\n'
        'kS9b4zjfS2KhNdkmCeOYU0tJpNfwmOTI90qeUdUCgYBomvPD+SNYr24OVN5oRLZ7\r\n'
        'ia6/ptZuilh+s8dVYbs08agZ2GcGd3vT6OGAwSJNlI1TxVfDa7umsBHeRn6QCnUN\r\n'
        '3CWp51g7MWw4lw8DRRmFs5HKsHLfSRuWX/u7oJqcWbpfhXInEKl6N3uMo3DpwJMU\r\n'
        '/Wx+FaDk1UnkRROQ/ATrowKBgEsM9fpv75kxTf6btWyu7xe0uZzVay+ANDhYhLBp\r\n'
        'YgpriVszinS9eA4mMXLb58Nx+qk9nSmWX1drW7HuTffiXnHZXVI37qgKCyHu3Q+3\r\n'
        'SouNmDpUwvUF5qr04daIZybvKZkRVxGUBlJvwVYaCG9v1j5I2r+mEpILglB7eB0X\r\n'
        'dmMBAoGABocuCOEOq+oyLDALwzMXU8gOf3IL1Q1/BWwsdoANoh6i179psxgE4JXT\r\n'
        'oWcpXZQQqub8ngwE6uR9fpd3m6N/PL4T55vbDDyjPKmrL2ttC2gOtx9KrpPh+Z7L\r\n'
        'QRo4BE48nHJJrystKHfFlaH2G7JxHNgMBYVADyttN09qEoav8Os=\r\n'
        '-----END RSA PRIVATE KEY-----'
    )


@pytest.fixture
def public_key():
    return (
        '-----BEGIN PUBLIC KEY-----\r\n'
        'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtpS1ZmfVKVP5KofIhMBP\r\n'
        '0tSWc4qlh6fm2lrZSkuKxUjEaWjzZSzs72gEIGxraWusMdoRuV54xsWRyf5KeZT0\r\n'
        'S+I5Prle3Idi3gICiO4NwvMk6JwSBcJWwmSLFEKyUSnB2CtfiGc0/5rQCpcEt/Dn\r\n'
        '5iM+BNn7fqpoLIbks8rXKUIj8+qMVqkTXsEKeKinE23t1ykMldsNaaOH+hvGti5J\r\n'
        't2DMnH1JjoXdDXfxvSP/0gjUYb0ektudYFXoA6wekmQyJeImvgx4Myz1I4iHtkY/\r\n'
        'Cp7J4Mn1ejZ6HNmyvoTE/4OuY1uCeYv4UyXFc1s1uUyYtj4z57qsHGsS4dQ3A2MJ\r\n'
        'swIDAQAB\r\n'
        '-----END PUBLIC KEY-----\r\n'
    )


@pytest.fixture
def expected_jws_signature():
    return (
        b'eyJhbGciOiJSUzI1NiIsImI2NCI6ZmFsc2UsImNyaXQiOlsiYjY0Il19..fZRkjTT'
        b'rcXdUovHjghM6JvlMhJuR1s8X1F4Uy_F4oMhZ9KtF2Zp78lYSOI7OxB5uoTu8FpQH'
        b'vy-dz3N4nLhoSWAi2_HrxZG_2DyctUUB_8pRKYBmIdIgpOlEMjIreOvXyM6A32gR-'
        b'PdbzoQq14yQbbfxk12jyZSwcaNu29gXnW_uO7ku1GSV_juWE5E_yIstvEB1GG8ApU'
        b'GIuzRJDrAAa8KBkHN7Rdfhc8rJMOeSZI0dc_A-Y7t0M0RtrgvV_FhzM40K1pwr1YU'
        b'Z5y1N4QV13M5u5qJ_lBK40WtWYL5MbJ58Qqk_-Q8l1dp6OCmoMvwdc7FmMsPigmyk'
        b'lqo46uyjjw'
    )


@pytest.fixture
def jld_document():
    return {
        '@context': {
            'homepage': 'schema:url',
            'image': 'schema:image',
            'name': 'schema:name',
            'schema': 'http://schema.org/'
        },
        'homepage': 'https://manu.sporny.org/',
        'image': 'https://manu.sporny.org/images/manu.png',
        'name': 'Manu Sporny'
    }


@pytest.fixture
def expected_jld_document_signed():
    return {
        '@context': {
            'homepage': 'schema:url',
            'image': 'schema:image',
            'name': 'schema:name',
            'schema': 'http://schema.org/'
        },
        'homepage': 'https://manu.sporny.org/',
        'image': 'https://manu.sporny.org/images/manu.png',
        'name': 'Manu Sporny',
        'signature': {
            'type': 'RsaSignatureSuite2017',
            # when testing we should first pop the created key since its
            # dynamic
            # 'created': '2017-04-25T15:28:06Z',
            'signatureValue': (
                'eyJhbGciOiJSUzI1NiIsImI2NCI6ZmFsc2UsImNyaXQiOlsiYjY0Il19..J'
                'Gfjiu4FxNWjaW6YKukTLo7qlc8smzQTHHlm7L92FsYYJCwd5AzkyK-02SMx'
                'PdRuLF3fbyElH5U2ernGip5pEU7YWfrHVxU0nWwF_uUDVea9slH9ys55V_2'
                'DFe05fODEkxc2FD41E6VYJKoDmap8x5rfcc64Z4K5GZWqYm8XMWJu5pJS4k'
                'jIEIDShhVioGpNBDcd-VGheASpQaiyHtmB4viJBqo9Tbe0JBpmDWUSUboec'
                '9YMRRJKLElpgK-kZxCGZDHWYaQMuIPdskbMDCf-fe5tWDei9PPBqVRyagQ7'
                'stEF7OYW-3T2G3J7dN1CmEoczhpP_mKLI2n16EphQbNGCw'
            )
        }
    }
