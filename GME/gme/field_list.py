# coding:utf-8

fieldFir = ["_id", "innerCode", "trade_date", "symbol", "name", "sec_type", "list_sec", "chi_spel",
                "area_code", "area_name", "is_st", "is_margin", "list_date", "act_date", "div_year",
                "div_date", "div_pct", "mkt_num", "a_mkt_num", "totl_num", "in_hld_pct", "in_chng_pct",
                "mng_hld_pct", "mng_chng_pct", "perf_idx", "val_idx", "fin_idx", "fcst_idx", "mkt2_idx",
                "org_hld_pct", "org_chng_pct", "staff_num", "sw_indu_name", "sw_indu_code", "cname",
                "com_brief", "mkt_idx", "signal_normal", "candle_charts", "exchange", "pattern",
                "status_type", "free_a_mkt_num"]
perf_idx = ["expr_enddate","avg_vol_3month","chng_pct_3month","chng_pct_year_sofar","chng_pct_6month",
                 "volat_3mon","chng_pct","yld_avg_month","beta","fac_tclose","volat_6mon","volat_mon",
                 "volat_12mon","chng_pct_month","keep_days","chng_pct_year","volat_week","close_px","atr",
                 "exchr_month","exchr_week","exchr_6month","exchr_3month","exchr_year"]
val_idx = ["val_enddate"]
fin_idx = ["sale_qua_rr","sel_rint","eps_qua_rr","sel_nint","du_roe","sale","roic","tot_liab_equ",
                "quick_ratio","sale_gr_5year","liab_equ","tot_revenue","current_ratio","roa","eps_5year",
                "tr_tp","fin_enddate"]
fcst_idx = ["fcst_stat_year","real_eps_chng","fir_fcst_eps_chng","fcst_eps_chng_next3",
                 "fcst_eps_next1","expect_price_med","rating_syn","fcst_eps_next_qua","expect_price_hight",
                 "expect_price_low","es_3year","expect_price_chng_pct","expect_price_high"]
mkt2_idx = ["eps_forecast","eps_ttm","fcps","sps","cps","mic_ttm","bps","eps_lyr","fc_ttm",
                 "exchr_bef_2day","es_3year","net_asset","low_10day","low_30day","high_52week",
                 "high_30day","low_20day","ps_cash_bt_1year","high_20day","cash_ttm","low_60day",
                 "high_60day","low_52week","high_120day","mic_lyr","high_10day","low_120day",
                 "lclose_week","low_9day","low_19day","low_29day","low_59day","low_119day","high_9day",
                 "high_19day","high_29day","high_59day","high_119day"]
mkt_idx = ["is_stop","rela_low_60day","ma120_cross_ma250_below","price_cross_ma20_below",
                "rela_low_20day","rela_ma60","ma30_bfac","ma120_bfac","rela_high_20day","price_cross_ma250_above",
                "is_limit_up","rela_ma120","ma20_cross_ma60_above","peg","ma10_dif_ma30","ma10_cross_ma30_above",
                "price_cross_ma10_below","div_rate","rela_high_10day","price_cash","ma60_cross_ma120_above",
                "rela_ma30","chng_pct_from_open","ma5_cross_ma10_below","mktcap","prange","rela_low_120day",
                "price_cross_ma20_above","rsi_14","price_cross_ma120_below","ma20","ma60_cross_ma120_below",
                "ma120_cross_ma250_above","price","rela_low_10day","ma30_cross_ma120_above","rela_ma250",
                "ma10_afac","ma20_cross_ma30_below","price_cross_ma60_below","price_cross_ma5_below",
                "mktcap_a","amount","high_px","rela_ma10","ma30","exchr","pe_lyr","ma120","limit_up",
                "price_cross_ma30_below","rela_low_30day","ma30_cross_ma60_below","ma20_afac","tcap","ps",
                "ma30_cross_ma120_below","chg","ma20_bfac","pb","pc","ma5_cross_ma20_above","ma60_cross_ma250_below",
                "price_cross_ma10_above","ma5_cross_ma10_above","ma20_cross_ma60_below","rela_ma5",
                "price_cross_ma30_above","ma60_bfac","rela_high_120day","volume","ma60_cross_ma250_above",
                "cur_chng_pct","ma60_afac","price_cross_ma250_below","ma250","low_px","prev_close_px",
                "ma10_bfac","ma10","ma10_cross_ma20_above","ma5","limit_down","ma10_cross_ma30_below",
                "pe_ttm","rela_high_60day","ma10_cross_ma20_below","rela_high_30day","ma5_cross_ma20_below",
                "rela_ma20","ma5_bfac","is_limit_down","ma60","price_cross_ma60_above","ma30_afac",
                "ma20_cross_ma30_above","expect_price_chng_pct","ma30_cross_ma60_above","ma120_afac","gap",
                "open_px","ma250_bfac","price_cross_ma120_above","ma250_afac","chng_pct_week","price_cross_ma5_above",
                "rela_volume","ma5_afac","rela_low_52week","rela_high_52week","fir_fcst_pe","rela_low_9day",
                "rela_low_19day","rela_low_29day","rela_low_59day","rela_low_119day","rela_high_9day","rela_high_19day",
                "rela_high_29day","rela_high_59day","rela_high_119day","keep_days_today"]
signal_normal = ["signal_normal_2","signal_normal_1","signal_normal_30","signal_normal_31",
                      "signal_normal_29","signal_normal_28","signal_normal_17","signal_normal_8",
                      "signal_normal_9","signal_normal_7","signal_normal_33","signal_normal_4","signal_normal_3",
                      "signal_normal_21","signal_normal_20","signal_normal_18","signal_normal_19","signal_normal_13",
                      "signal_normal_10","signal_normal_32","signal_normal_34","signal_normal_35","signal_normal_14",
                      "signal_normal_16","signal_normal_15","signal_normal_11","signal_normal_5","signal_normal_12",
                      "signal_normal_25","signal_normal_24","signal_normal_23","signal_normal_22","signal_normal_6"]
candle_charts = ["candle_charts_18","candle_charts_19","candle_charts_5","candle_charts_10",
                      "candle_charts_11","candle_charts_12","candle_charts_13","candle_charts_14","candle_charts_15",
                      "candle_charts_16","candle_charts_20","candle_charts_8","candle_charts_9","candle_charts_6",
                      "candle_charts_7","candle_charts_4","candle_charts_17","candle_charts_2","candle_charts_3",
                      "candle_charts_1"]