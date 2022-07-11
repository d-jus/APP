import unittest, pytest
import neural_net, prepare
from numpy import array

def test_main_pre():
    compute_pre = neural_net._pre(
    [56,	9.1,	0,	0.3,	0.5,	0.6,	20,	20,	30,	1.1,	0,	0]
    )
    assert compute_pre == 0.9247


def test_main_mu():
    compute_mu = neural_net._mu(
    [56,	9.1,	0,	0.3,	0.5,	0.6,	20,	20,	30,	1.1,	6.4,	1.6,	0,	2.5,	0,	0]
    )
    assert compute_mu == 0.66

def test_recon_length():
    t_ = prepare.recon_length([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
    assert t_ == True

def test_clean_vector_long_lv():
    "for long vector (16 elements)"
    t_ = prepare.clean_vector([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
    assert all(t_ == array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16]))

def test_clean_vector_long_sh():
    "for short vector (12 elements)"
    t_ = prepare.clean_vector([1,2,3,4,5,6,7,8,9,10,15,16])
    assert all(t_ == array([1,2,3,4,5,6,7,8,9,10,15,16]))

def test_clean_vector_sh():
    t_ = prepare.clean_vector([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], short=True)
    assert all(t_ == array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 15, 16]))




"""
def test_clean_vector_err():
    with pytest.raises(ValueError):
        prepare.clean_vector([1,2,3,4,5,15,16])
   """ 