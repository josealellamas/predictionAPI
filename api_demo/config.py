from sklearn.decomposition import PCA

#Varibles para transformación YEO JOHNSON
NUMERICALS_YEO_JOHNSON_VARS = ['total_intl_calls']

#Variables para binarización por sesgo fuerte
BINARIZE_VARS = ['number_vmail_messages']

#Variables categoricas a codificar sin ordinalidad
CATEGORICAL_VARS = ['state', 'area_code']

#Variables para OHE
OHE_VARS = ['international_plan', 'voice_mail_plan']

#PCA
pca = PCA(n_components=1)

#Variables seleccionadas para uso
FEATURES = ['state',
            'account_length',
            'area_code',
            'international_plan',
            'voice_mail_plan',
            'number_vmail_messages',
            'total_day_minutes',
            'total_day_calls',
            'total_day_charge',
            'total_eve_minutes',
            'total_eve_calls',
            'total_eve_charge',
            'total_night_minutes',
            'total_night_calls',
            'total_night_charge',
            'total_intl_minutes',
            'total_intl_calls',
            'total_intl_charge',
            'number_customer_service_calls']