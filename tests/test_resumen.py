import json
import sys
import tempfile
import unittest
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
import resumen  # noqa: E402


class TestResumen(unittest.TestCase):
    def setUp(self):
        self.ventas = resumen.leer_ventas()

    def test_cantidad_de_operaciones(self):
        self.assertEqual(len(self.ventas), 12)

    def test_total_general(self):
        self.assertEqual(resumen.total_general(self.ventas), Decimal("1845.00"))

    def test_totales_por_sede(self):
        totales = resumen.totales_por_sede(self.ventas)
        self.assertEqual(totales["Lima"], Decimal("814.00"))
        self.assertEqual(totales["Ica"], Decimal("555.00"))
        self.assertEqual(totales["Arequipa"], Decimal("476.00"))

    def test_ficha_por_sede(self):
        esperado = {"Lima": "814.00", "Ica": "550.00", "Arequipa": "476.00"}
        totales = resumen.totales_por_sede(self.ventas)
        for sede, monto in esperado.items():
            with self.subTest(sede=sede):
                self.assertEqual(totales[sede], Decimal(monto))

    def test_resumen_serializable(self):
        datos = resumen.construir_resumen(self.ventas)
        with tempfile.TemporaryDirectory() as tmp:
            ruta = Path(tmp) / "resumen.json"
            ruta.write_text(json.dumps(datos), encoding="utf-8")
            self.assertEqual(json.loads(ruta.read_text())["total"], "1845.00")


if __name__ == "__main__":
    unittest.main()
