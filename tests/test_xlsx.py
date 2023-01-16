from potyk_doc.xlsx import render_xlsx_from_html, xlsx_values


def test_render_xlsx_from_html():
    stream = render_xlsx_from_html("""<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Simple table</title>
    </head>
    <body>
        <table>
            <tbody>
                <tr>
                    <td>1</td>
                    <td>2</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>4</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>""")

    assert xlsx_values(stream) == ((1, 2), (3, 4))
