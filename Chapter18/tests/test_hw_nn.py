import unittest

from hw.libhw import nn


class TestNN(unittest.TestCase):
    def test_simple(self):
        a = [
            [0.568, 0.831963, 0.500232, 0.779808],
            [0.85657, 0.884498, 0.939402, 0.373441],
            [0.788641, 0.510002, 0.0541478, 0.858826],
        ]
        b = [
            [0.490521, 0.68652],
            [0.0899963, 0.85232],
            [0.0716166, 0.331572],
            [0.872228, 0.510125],
        ]
        r = nn.matmul(a, b)
        self.assertEqual(
            r,
            [
                [1.0694848070121, 1.6627045448639999],
                [0.8927695941486, 1.843908761829],
                [1.18571323061508, 1.4321652315516],
            ],
        )
