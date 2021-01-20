import qrcode

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
)


def generate_qr(text, f_name):
    try:
        f_name = str(f_name)
        if not (text == '' and f_name == ''):
            qr.add_data(text)
            qr.make(fit=True)
            img = qr.make_image()
            img.save(f'QR_Codes/{f_name}')
            return 1
        return 0
    except:
        return 0



