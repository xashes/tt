from tt.portfolio import Portfolio

import pandas as pd


sample_portfolio = Portfolio()

def test_blotter():
    return sample_portfolio.blotter

def test_positions():
    return sample_portfolio.positions
