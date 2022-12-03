#!/usr/bin/env python
# -*- coding: utf-8 -*-


def calculate_pay(periods):
    return sum(periods) * 3


def test_add_employee():
    assert add_employee('andy') is True


def test_change_employee():
    assert change_employee('andy', 'fred') is True


def test_calculate_pay():
    assert calculate_pay([10, 10]) == 60
