# LoanProductData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_moves_out_of_npa_only_on_arrears_completion** | **bool** |  | [optional] 
**accounting_mapping_options** | **dict(str, list[GLAccountData])** |  | [optional] 
**accounting_mappings** | **dict(str, object)** |  | [optional] 
**accounting_rule** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**accounting_rule_options** | [**list[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**advanced_payment_allocation_future_installment_allocation_rules** | [**list[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**advanced_payment_allocation_transaction_types** | [**list[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**advanced_payment_allocation_types** | [**list[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**allow_approved_disbursed_amounts_over_applied** | **bool** |  | [optional] 
**allow_attribute_overrides** | [**LoanProductConfigurableAttributes**](LoanProductConfigurableAttributes.md) |  | [optional] 
**allow_partial_period_interest_calculation** | **bool** |  | [optional] 
**allow_variable_installments** | **bool** |  | [optional] 
**amortization_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**amortization_type_options** | [**list[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**annual_interest_rate** | **float** |  | [optional] 
**can_define_installment_amount** | **bool** |  | [optional] 
**can_use_for_topup** | **bool** |  | [optional] 
**charge_options** | [**list[ChargeData]**](ChargeData.md) |  | [optional] 
**charges** | [**list[ChargeData]**](ChargeData.md) |  | [optional] 
**close_date** | **date** |  | [optional] 
**compounding_to_be_posted_as_transaction** | **bool** |  | [optional] 
**credit_allocation** | [**list[CreditAllocationData]**](CreditAllocationData.md) |  | [optional] 
**credit_allocation_allocation_types** | [**list[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**credit_allocation_transaction_types** | [**list[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**currency** | [**CurrencyData**](CurrencyData.md) |  | [optional] 
**currency_options** | [**list[CurrencyData]**](CurrencyData.md) |  | [optional] 
**days_in_month_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**days_in_month_type_options** | [**list[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**days_in_year_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**days_in_year_type_options** | [**list[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**default_differential_lending_rate** | **float** |  | [optional] 
**delinquency_bucket** | [**DelinquencyBucketData**](DelinquencyBucketData.md) |  | [optional] 
**delinquency_bucket_options** | [**list[DelinquencyBucketData]**](DelinquencyBucketData.md) |  | [optional] 
**description** | **str** |  | [optional] 
**disallow_expected_disbursements** | **bool** |  | [optional] 
**disbursed_amount_percentage_for_down_payment** | **float** |  | [optional] 
**due_days_for_repayment_event** | **int** |  | [optional] 
**enable_accrual_activity_posting** | **bool** |  | [optional] 
**enable_auto_repayment_for_down_payment** | **bool** |  | [optional] 
**enable_down_payment** | **bool** |  | [optional] 
**enable_installment_level_delinquency** | **bool** |  | [optional] 
**equal_amortization** | **bool** |  | [optional] 
**external_id** | **str** |  | [optional] 
**fee_to_income_account_mappings** | [**list[ChargeToGLAccountMapper]**](ChargeToGLAccountMapper.md) |  | [optional] 
**fixed_length** | **int** |  | [optional] 
**fixed_principal_percentage_per_installment** | **float** |  | [optional] 
**floating_interest_rate_calculation_allowed** | **bool** |  | [optional] 
**floating_rate_id** | **int** |  | [optional] 
**floating_rate_name** | **str** |  | [optional] 
**floating_rate_options** | [**list[FloatingRateData]**](FloatingRateData.md) |  | [optional] 
**fund_id** | **int** |  | [optional] 
**fund_name** | **str** |  | [optional] 
**fund_options** | [**list[FundData]**](FundData.md) |  | [optional] 
**grace_on_arrears_ageing** | **int** |  | [optional] 
**grace_on_interest_charged** | **int** |  | [optional] 
**grace_on_interest_payment** | **int** |  | [optional] 
**grace_on_principal_payment** | **int** |  | [optional] 
**hold_guarantee_funds** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**in_arrears_tolerance** | **float** |  | [optional] 
**include_in_borrower_cycle** | **bool** |  | [optional] 
**installment_amount_in_multiples_of** | **int** |  | [optional] 
**interest_calculation_period_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**interest_calculation_period_type_options** | [**list[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**interest_rate_differential** | **float** |  | [optional] 
**interest_rate_frequency_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**interest_rate_frequency_type_options** | [**list[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**interest_rate_per_period** | **float** |  | [optional] 
**interest_rate_variations_for_borrower_cycle** | [**list[LoanProductBorrowerCycleVariationData]**](LoanProductBorrowerCycleVariationData.md) |  | [optional] 
**interest_recalculation_compounding_type_options** | [**list[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**interest_recalculation_data** | [**LoanProductInterestRecalculationData**](LoanProductInterestRecalculationData.md) |  | [optional] 
**interest_recalculation_day_of_week_type_options** | [**list[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**interest_recalculation_enabled** | **bool** |  | [optional] 
**interest_recalculation_frequency_type_options** | [**list[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**interest_recalculation_nth_day_type_options** | [**list[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**interest_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**interest_type_options** | [**list[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**is_allow_partial_period_interest_calculation** | **bool** |  | [optional] 
**is_equal_amortization** | **bool** |  | [optional] 
**is_floating_interest_rate_calculation_allowed** | **bool** |  | [optional] 
**is_interest_recalculation_enabled** | **bool** |  | [optional] 
**is_linked_to_floating_interest_rates** | **bool** |  | [optional] 
**is_rates_enabled** | **bool** |  | [optional] 
**linked_to_floating_interest_rates** | **bool** |  | [optional] 
**loan_product_configurable_attributes** | [**LoanProductConfigurableAttributes**](LoanProductConfigurableAttributes.md) |  | [optional] 
**loan_schedule_processing_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**loan_schedule_processing_type_options** | [**list[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**loan_schedule_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**loan_schedule_type_options** | [**list[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**max_differential_lending_rate** | **float** |  | [optional] 
**max_interest_rate_per_period** | **float** |  | [optional] 
**max_number_of_repayments** | **int** |  | [optional] 
**max_principal** | **float** |  | [optional] 
**max_tranche_count** | **int** |  | [optional] 
**maximum_gap** | **int** |  | [optional] 
**min_differential_lending_rate** | **float** |  | [optional] 
**min_interest_rate_per_period** | **float** |  | [optional] 
**min_number_of_repayments** | **int** |  | [optional] 
**min_principal** | **float** |  | [optional] 
**minimum_days_between_disbursal_and_first_repayment** | **int** |  | [optional] 
**minimum_gap** | **int** |  | [optional] 
**multi_disburse_loan** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**number_of_repayment_variations_for_borrower_cycle** | [**list[LoanProductBorrowerCycleVariationData]**](LoanProductBorrowerCycleVariationData.md) |  | [optional] 
**number_of_repayments** | **int** |  | [optional] 
**outstanding_loan_balance** | **float** |  | [optional] 
**over_applied_calculation_type** | **str** |  | [optional] 
**over_applied_number** | **int** |  | [optional] 
**over_due_days_for_repayment_event** | **int** |  | [optional] 
**overdue_days_for_npa** | **int** |  | [optional] 
**payment_allocation** | [**list[AdvancedPaymentData]**](AdvancedPaymentData.md) |  | [optional] 
**payment_channel_to_fund_source_mappings** | [**list[PaymentTypeToGLAccountMapper]**](PaymentTypeToGLAccountMapper.md) |  | [optional] 
**payment_type_options** | [**list[PaymentTypeData]**](PaymentTypeData.md) |  | [optional] 
**penalty_options** | [**list[ChargeData]**](ChargeData.md) |  | [optional] 
**penalty_to_income_account_mappings** | [**list[ChargeToGLAccountMapper]**](ChargeToGLAccountMapper.md) |  | [optional] 
**pre_closure_interest_calculation_strategy_options** | [**list[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**principal** | **float** |  | [optional] 
**principal_threshold_for_last_installment** | **float** |  | [optional] 
**principal_variations_for_borrower_cycle** | [**list[LoanProductBorrowerCycleVariationData]**](LoanProductBorrowerCycleVariationData.md) |  | [optional] 
**product_guarantee_data** | [**LoanProductGuaranteeData**](LoanProductGuaranteeData.md) |  | [optional] 
**rate_options** | [**list[RateData]**](RateData.md) |  | [optional] 
**rates** | [**list[RateData]**](RateData.md) |  | [optional] 
**rates_enabled** | **bool** |  | [optional] 
**recurring_moratorium_on_principal_periods** | **int** |  | [optional] 
**repayment_every** | **int** |  | [optional] 
**repayment_frequency_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**repayment_frequency_type_options** | [**list[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**repayment_start_date_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**repayment_start_date_type_options** | [**list[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**reschedule_strategy_type_options** | [**list[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**short_name** | **str** |  | [optional] 
**start_date** | **date** |  | [optional] 
**status** | **str** |  | [optional] 
**supported_interest_refund_types** | [**list[StringEnumOptionData]**](StringEnumOptionData.md) |  | [optional] 
**supported_interest_refund_types_options** | [**list[StringEnumOptionData]**](StringEnumOptionData.md) |  | [optional] 
**sync_expected_with_disbursement_date** | **bool** |  | [optional] 
**transaction_processing_strategy_code** | **str** |  | [optional] 
**transaction_processing_strategy_name** | **str** |  | [optional] 
**transaction_processing_strategy_options** | [**list[TransactionProcessingStrategyData]**](TransactionProcessingStrategyData.md) |  | [optional] 
**use_borrower_cycle** | **bool** |  | [optional] 
**value_condition_type_options** | [**list[EnumOptionData]**](EnumOptionData.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

