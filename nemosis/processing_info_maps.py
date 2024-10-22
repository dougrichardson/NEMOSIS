import os
from . import query_wrappers

from nemosis import (
    filters,
    downloader,
    write_file_names,
    date_generators,
)


setup = {
    "DISPATCHLOAD": None,
    "NEXT_DAY_DISPATCHLOAD": None,
    "TRADINGLOAD": None,
    "TRADINGPRICE": None,
    "TRADINGREGIONSUM": None,
    "TRADINGINTERCONNECT": None,
    "DISPATCHPRICE": None,
    "DISPATCH_UNIT_SCADA": None,
    "DISPATCHCONSTRAINT": None,
    "DUDETAILSUMMARY": None,
    "PARTICIPANT": None,
    "DUDETAIL": None,
    "GENCONDATA": None,
    "SPDREGIONCONSTRAINT": None,
    "SPDCONNECTIONPOINTCONSTRAINT": None,
    "SPDINTERCONNECTORCONSTRAINT": None,
    "FCAS_4_SECOND": None,
    "ELEMENTS_FCAS_4_SECOND": None,
    "VARIABLES_FCAS_4_SECOND": None,
    "Generators and Scheduled Loads": None,
    "BIDDAYOFFER_D": query_wrappers.dispatch_date_setup,
    "BIDPEROFFER_D": None,
    "FCAS_4s_SCADA_MAP": None,
    "DISPATCHINTERCONNECTORRES": None,
    "DISPATCHREGIONSUM": None,
    "LOSSMODEL": None,
    "LOSSFACTORMODEL": None,
    "MNSP_DAYOFFER": query_wrappers.dispatch_date_setup,
    "MNSP_PEROFFER": query_wrappers.dispatch_half_hour_setup,
    "MNSP_INTERCONNECTOR": None,
    "INTERCONNECTOR": None,
    "INTERCONNECTORCONSTRAINT": None,
    "MARKET_PRICE_THRESHOLDS": None,
    "DAILY_REGION_SUMMARY": None,
    "ROOFTOP_PV_ACTUAL": None,
}

search_type = {
    "DISPATCHLOAD": "start_to_end",
    "NEXT_DAY_DISPATCHLOAD": "start_to_end",
    "TRADINGLOAD": "start_to_end",
    "TRADINGPRICE": "start_to_end",
    "TRADINGREGIONSUM": "start_to_end",
    "TRADINGINTERCONNECT": "start_to_end",
    "DISPATCHPRICE": "start_to_end",
    "DISPATCH_UNIT_SCADA": "start_to_end",
    "DISPATCHCONSTRAINT": "start_to_end",
    "DUDETAILSUMMARY": "end",
    "PARTICIPANT": "all",
    "DUDETAIL": "all",
    "GENCONDATA": "all",
    "SPDREGIONCONSTRAINT": "all",
    "SPDCONNECTIONPOINTCONSTRAINT": "all",
    "SPDINTERCONNECTORCONSTRAINT": "all",
    "FCAS_4_SECOND": "start_to_end",
    "ELEMENTS_FCAS_4_SECOND": None,
    "VARIABLES_FCAS_4_SECOND": None,
    "Generators and Scheduled Loads": None,
    "BIDDAYOFFER_D": "start_to_end",
    "BIDPEROFFER_D": "start_to_end",
    "FCAS_4s_SCADA_MAP": None,
    "DISPATCHINTERCONNECTORRES": "start_to_end",
    "DISPATCHREGIONSUM": "start_to_end",
    "LOSSMODEL": "all",
    "LOSSFACTORMODEL": "all",
    "MNSP_DAYOFFER": "start_to_end",
    "MNSP_PEROFFER": "start_to_end",
    "MNSP_INTERCONNECTOR": "all",
    "INTERCONNECTOR": "all",
    "INTERCONNECTORCONSTRAINT": "all",
    "MARKET_PRICE_THRESHOLDS": "all",
    "DAILY_REGION_SUMMARY": 'start_to_end',
    "ROOFTOP_PV_ACTUAL": "start_to_end",
}

date_cols = {
    "DISPATCHLOAD": ["SETTLEMENTDATE"],
    "NEXT_DAY_DISPATCHLOAD": ["SETTLEMENTDATE"],
    "TRADINGLOAD": ["SETTLEMENTDATE"],
    "TRADINGPRICE": ["SETTLEMENTDATE"],
    "TRADINGREGIONSUM": ["SETTLEMENTDATE"],
    "TRADINGINTERCONNECT": ["SETTLEMENTDATE"],
    "DISPATCHPRICE": ["SETTLEMENTDATE"],
    "DISPATCH_UNIT_SCADA": ["SETTLEMENTDATE"],
    "DISPATCHCONSTRAINT": ["SETTLEMENTDATE"],
    "DUDETAILSUMMARY": ["START_DATE", "END_DATE"],
    "PARTICIPANT": ["LASTCHANGED"],
    "DUDETAIL": ["EFFECTIVEDATE"],
    "GENCONDATA": ["EFFECTIVEDATE"],
    "SPDREGIONCONSTRAINT": ["EFFECTIVEDATE"],
    "SPDCONNECTIONPOINTCONSTRAINT": ["EFFECTIVEDATE"],
    "SPDINTERCONNECTORCONSTRAINT": ["EFFECTIVEDATE"],
    "FCAS_4_SECOND": ["TIMESTAMP"],
    "ELEMENTS_FCAS_4_SECOND": None,
    "VARIABLES_FCAS_4_SECOND": None,
    "Generators and Scheduled Loads": None,
    "BIDDAYOFFER_D": ["SETTLEMENTDATE"],
    "BIDPEROFFER_D": ["INTERVAL_DATETIME"],
    "FCAS_4s_SCADA_MAP": None,
    "DISPATCHINTERCONNECTORRES": ["SETTLEMENTDATE"],
    "DISPATCHREGIONSUM": ["SETTLEMENTDATE"],
    "LOSSMODEL": ["EFFECTIVEDATE"],
    "LOSSFACTORMODEL": ["EFFECTIVEDATE"],
    "MNSP_DAYOFFER": ["SETTLEMENTDATE"],
    "MNSP_PEROFFER": ["SETTLEMENTDATE", "PERIODID"],
    "MNSP_INTERCONNECTOR": ["EFFECTIVEDATE"],
    "INTERCONNECTOR": ["LASTCHANGED"],
    "INTERCONNECTORCONSTRAINT": ["EFFECTIVEDATE"],
    "MARKET_PRICE_THRESHOLDS": ["EFFECTIVEDATE"],
    "DAILY_REGION_SUMMARY": ['SETTLEMENTDATE'],
    "ROOFTOP_PV_ACTUAL": ["INTERVAL_DATETIME"],
}

filter = {
    "DISPATCHLOAD": filters.filter_on_settlementdate,
    "NEXT_DAY_DISPATCHLOAD": filters.filter_on_settlementdate,
    "TRADINGLOAD": filters.filter_on_settlementdate,
    "TRADINGPRICE": filters.filter_on_settlementdate,
    "TRADINGREGIONSUM": filters.filter_on_settlementdate,
    "TRADINGINTERCONNECT": filters.filter_on_settlementdate,
    "DISPATCHPRICE": filters.filter_on_settlementdate,
    "DISPATCH_UNIT_SCADA": filters.filter_on_settlementdate,
    "DISPATCHCONSTRAINT": filters.filter_on_settlementdate,
    "DUDETAILSUMMARY": filters.filter_on_start_and_end_date,
    "PARTICIPANT": filters.filter_on_last_changed,
    "DUDETAIL": filters.filter_on_effective_date,
    "GENCONDATA": filters.filter_on_effective_date,
    "SPDREGIONCONSTRAINT": filters.filter_on_effective_date,
    "SPDCONNECTIONPOINTCONSTRAINT": filters.filter_on_effective_date,
    "SPDINTERCONNECTORCONSTRAINT": filters.filter_on_effective_date,
    "FCAS_4_SECOND": filters.filter_on_timestamp,
    "ELEMENTS_FCAS_4_SECOND": None,
    "VARIABLES_FCAS_4_SECOND": None,
    "Generators and Scheduled Loads": None,
    "BIDDAYOFFER_D": filters.filter_on_settlementdate,
    "BIDPEROFFER_D": filters.filter_on_interval_datetime,
    "FCAS_4s_SCADA_MAP": None,
    "DISPATCHINTERCONNECTORRES": filters.filter_on_settlementdate,
    "DISPATCHREGIONSUM": filters.filter_on_settlementdate,
    "LOSSMODEL": filters.filter_on_effective_date,
    "LOSSFACTORMODEL": filters.filter_on_effective_date,
    "MNSP_DAYOFFER": filters.filter_on_settlementdate,
    "MNSP_PEROFFER": filters.filter_on_date_and_peroid,
    "MNSP_INTERCONNECTOR": filters.filter_on_effective_date,
    "INTERCONNECTOR": filters.filter_on_last_changed,
    "INTERCONNECTORCONSTRAINT": filters.filter_on_effective_date,
    "MARKET_PRICE_THRESHOLDS": filters.filter_on_effective_date,
    "DAILY_REGION_SUMMARY": filters.filter_on_settlementdate,
    "ROOFTOP_PV_ACTUAL": filters.filter_on_interval_datetime,
}

finalise = {
    "DISPATCHLOAD": None,
    "NEXT_DAY_DISPATCHLOAD": None,
    "TRADINGLOAD": None,
    "TRADINGPRICE": None,
    "TRADINGREGIONSUM": None,
    "TRADINGINTERCONNECT": None,
    "DISPATCHPRICE": None,
    "DISPATCH_UNIT_SCADA": None,
    "DISPATCHCONSTRAINT": [
        query_wrappers.convert_genconid_effectivedate_to_datetime_format
    ],
    "DUDETAILSUMMARY": [
        query_wrappers.most_recent_records_before_start_time,
        query_wrappers.drop_duplicates_by_primary_key,
    ],
    "PARTICIPANT": [
        query_wrappers.most_recent_records_before_start_time,
        query_wrappers.drop_duplicates_by_primary_key,
    ],
    "DUDETAIL": [
        query_wrappers.most_recent_records_before_start_time,
        query_wrappers.drop_duplicates_by_primary_key,
    ],
    "GENCONDATA": [
        query_wrappers.most_recent_records_before_start_time,
        query_wrappers.drop_duplicates_by_primary_key,
    ],
    "SPDREGIONCONSTRAINT": [query_wrappers.most_recent_records_before_start_time],
    "SPDCONNECTIONPOINTCONSTRAINT": [
        query_wrappers.most_recent_records_before_start_time,
        query_wrappers.drop_duplicates_by_primary_key,
    ],
    "SPDINTERCONNECTORCONSTRAINT": [
        query_wrappers.most_recent_records_before_start_time,
        query_wrappers.drop_duplicates_by_primary_key,
    ],
    "FCAS_4_SECOND": [query_wrappers.fcas4s_finalise],
    "ELEMENTS_FCAS_4_SECOND": None,
    "VARIABLES_FCAS_4_SECOND": None,
    "Generators and Scheduled Loads": None,
    "BIDDAYOFFER_D": None,
    "BIDPEROFFER_D": None,
    "FCAS_4s_SCADA_MAP": None,
    "DISPATCHINTERCONNECTORRES": None,
    "DISPATCHREGIONSUM": None,
    "LOSSMODEL": [
        query_wrappers.most_recent_records_before_start_time,
        query_wrappers.drop_duplicates_by_primary_key,
    ],
    "LOSSFACTORMODEL": [
        query_wrappers.most_recent_records_before_start_time,
        query_wrappers.drop_duplicates_by_primary_key,
    ],
    "MNSP_DAYOFFER": [
        query_wrappers.most_recent_records_before_start_time,
        query_wrappers.drop_duplicates_by_primary_key,
    ],
    "MNSP_PEROFFER": [
        query_wrappers.most_recent_records_before_start_time,
        query_wrappers.drop_duplicates_by_primary_key,
    ],
    "MNSP_INTERCONNECTOR": [
        query_wrappers.most_recent_records_before_start_time,
        query_wrappers.drop_duplicates_by_primary_key,
    ],
    "INTERCONNECTOR": [
        query_wrappers.most_recent_records_before_start_time,
        query_wrappers.drop_duplicates_by_primary_key,
    ],
    "INTERCONNECTORCONSTRAINT": [
        query_wrappers.most_recent_records_before_start_time,
        query_wrappers.drop_duplicates_by_primary_key,
    ],
    "MARKET_PRICE_THRESHOLDS": None,
    "DAILY_REGION_SUMMARY": None,
    "ROOFTOP_PV_ACTUAL": [
        query_wrappers.drop_duplicates_by_primary_key
    ],
}

date_gen = {
    "MMS": date_generators.year_and_month_gen,
    "NEXT_DAY_DISPATCHLOAD": date_generators.current_gen,
    "BIDDING": date_generators.bid_table_gen,
    "DAILY_REGION_SUMMARY": date_generators.current_gen,
    "FCAS": date_generators.year_month_day_index_gen,
}

write_filename = {
    "MMS": write_file_names.write_mms_file_names,
    "NEXT_DAY_DISPATCHLOAD": write_file_names.write_file_names_current,
    "BIDDING": write_file_names.write_file_names_mms_and_current,
    "DAILY_REGION_SUMMARY": write_file_names.write_file_names_mms_and_current,
    "FCAS": write_file_names.write_file_names_fcas,
}

downloader = {
    "MMS": downloader.run,
    "NEXT_DAY_DISPATCHLOAD": downloader.run_next_dispatch_tables,
    "BIDDING": downloader.run_bid_tables,
    "DAILY_REGION_SUMMARY": downloader.run_next_day_region_tables,
    "FCAS": downloader.run_fcas4s,
}
