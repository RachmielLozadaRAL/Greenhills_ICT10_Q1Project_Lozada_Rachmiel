# Coffee Receipt
from pyscript import display, document

def createorder(e):
    document.getElementById("output").innerHTML = ""

    c1 = document.getElementById("coffee1")
    c2 = document.getElementById("coffee2")
    c3 = document.getElementById("coffee3")
    c4 = document.getElementById("coffee4")
    c5 = document.getElementById("coffee5")

    p1 = float(c1.value) * int(c1.checked)
    p2 = float(c2.value) * int(c2.checked)
    p3 = float(c3.value) * int(c3.checked)
    p4 = float(c4.value) * int(c4.checked)
    p5 = float(c5.value) * int(c5.checked)

    subtotal = round(p1 + p2 + p3 + p4 + p5, 2)
    vat = round(subtotal * 0.12, 2)
    total = round(subtotal + vat, 2)

    display(f'Subtotal: PHP {subtotal}', target="output", append=False)
    display(f'VAT: PHP {vat}', target="output", append=True)
    display(f'Total: PHP {total}', target="output", append=True)

# SKU Generator
def generate_sku(e):
    product = document.getElementById("sku-product").value
    product_number = int(document.getElementById("sku-number").value)
    sku = f"BEAN-{product}-{product_number:03d}"

    display(f"SKU: {sku}", target="sku-output", append=False) # Displays the SKU Code