# -*- coding: utf-8 -*-
from pytest_power.utils import Utils


def test_patchable_attributes():
    item = type('object', (object, ), {'yes': 'yes', '__no__': 'no'})
    result = Utils.patchable_attributes(item)
    assert list(result) == ['yes']


def test_patchable_attributes__excludes():
    item = type('object', (object, ), {'yes': 'yes', '__no__': 'no'})
    result = Utils.patchable_attributes(item, excludes=['yes'])
    assert list(result) == []


def test_patchable_attributes__includes():
    item = type('object', (object, ), {'yes': 'yes', '__no__': 'no'})
    result = Utils.patchable_attributes(item, includes=['__no__'])
    assert list(result) == ['yes', '__no__']
