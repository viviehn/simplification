import streamlit as st
import glob
import os

st.set_page_config(layout='wide')

display_type = st.selectbox('display_type', ['single', 'compare 2', 'compare 3'])

dirs = glob.glob('data/*')
dirs = list(filter(os.path.isdir, dirs))
dirs = [os.path.split(d)[1] for d in dirs]


val_models = ['857176_sporion2',
'985567_Stressless_armchair_10_seat',
'850051_SeaLife_ReefMaster_Underwater_Dive_Camera',
'705008_sparrow',
'619450_Speedlite_Low_Poly',
'1028102_Small_Kids_Backpack_01_001',
'981153_Stegosaurus_OBJ',
'457046_Squirrel',
'720949_Sport_Car',
'729162_Standar_Toon_Car',
'825045_825045_Stegosaurus',
'763464_Snow_Leopard',
'692144_strange_monster02',
'1003500_Space_Gloves_convert',
'798547_Sopwith',
'532386_Space_Shuttle_V2_obj',
'780936_Stylized_Rifle',
'897668_Spudtruck_Rocker',
'776303_stryker_stretcher_v03',
'719509_speed_indicator_obj',
'1001621_exacto',
'738716_Wheeled__Pipe_Cutter',
'768143_768143_spray',
'944359_Sonic',
'783340_Seahorse_and_Triton_Statue',
'856637_856637_SPERM_WHALE',
'1007380_Sci_Fi_Grenade',
'990880_Smiling_Buddah',
'1017250_Studebaker_Champion_Starlight',
'685865_Sofa_V46',
'941628_spchoopp',
'423705_Sparky',
'737975_S_Arm_OBJ',
'452829_styled_coat_2',
'783529_Statuette_14',
'574881_SeatModel4',
'843799_Spinosurus',
'750373_Showroom_Mannequin_12_obj',
]

non_val_models = list(set(dirs) - set(val_models))

dirs = val_models + non_val_models

opts = ['naive', 'beam', 'train_baseline_20220327_test', 'train_aug_20220327_test', 'train_base32_20220327_test', 
        'train_baseline_20220328_test', 'train_aug_w_rotate_20220328_test', 'train_aug_no_rot_20220328_test',
        'train_baseline_20220329_test',]

if display_type == 'single':
    algorithm = st.selectbox('algorithm', opts)
    percentiles = [10, 25, 50]
    stcols = st.columns(len(percentiles))
    for i, p in enumerate(percentiles):
        stcols[i].header(f'{p}% of strokes')
    for d in dirs:
        for i, p in enumerate(percentiles):
            fname = f'data/{d}/{algorithm}/pngs/{p}.png'
            if os.path.exists(fname):
                stcols[i].image(fname)
    'No more files found'

elif display_type == 'compare 2':
    p = st.selectbox('percent of lines', [10, 25, 50], 2)
    algorithm1 = st.selectbox('algorithm 1', opts)
    algorithm2 = st.selectbox('algorithm 2', opts, 1)
    stcols = st.columns(2)
    stcols[0].header(algorithm1)
    stcols[1].header(algorithm2)
    for d in val_models:

        algo1_fname = f'data/{d}/{algorithm1}/pngs/{p}.png'
        algo2_fname = f'data/{d}/{algorithm2}/pngs/{p}.png'
        algo1_fname
        algo2_fname
        if os.path.exists(algo1_fname) and os.path.exists(algo2_fname):

            stcols[0].image(algo1_fname, caption='Val')
            stcols[1].image(algo2_fname, caption='Val')
    for d in non_val_models:
        algo1_fname = f'data/{d}/{algorithm1}/pngs/{p}.png'
        algo2_fname = f'data/{d}/{algorithm2}/pngs/{p}.png'
        algo1_fname
        algo2_fname
        if os.path.exists(algo1_fname) and os.path.exists(algo2_fname):

            stcols[0].image(algo1_fname)
            stcols[1].image(algo2_fname)

    'No more file pairs found'

elif display_type == 'compare 3':
    p = st.selectbox('percent of lines', [10, 25, 50], 2)
    algorithm1 = st.selectbox('algorithm 1', opts)
    algorithm2 = st.selectbox('algorithm 2', opts, 1)
    algorithm3 = st.selectbox('algorithm 3', opts, 2)
    stcols = st.columns(3)
    stcols[0].header(algorithm1)
    stcols[1].header(algorithm2)
    stcols[2].header(algorithm3)
    for d in val_models:
        algo1_fname = f'data/{d}/{algorithm1}/pngs/{p}.png'
        algo2_fname = f'data/{d}/{algorithm2}/pngs/{p}.png'
        algo3_fname = f'data/{d}/{algorithm3}/pngs/{p}.png'
        if os.path.exists(algo1_fname) and os.path.exists(algo2_fname) and os.path.exists(algo3_fname):

            stcols[0].image(algo1_fname, caption='Val')
            stcols[1].image(algo2_fname, caption='Val')
            stcols[2].image(algo3_fname, caption='Val')
    for d in non_val_models:
        algo1_fname = f'data/{d}/{algorithm1}/pngs/{p}.png'
        algo2_fname = f'data/{d}/{algorithm2}/pngs/{p}.png'
        algo3_fname = f'data/{d}/{algorithm3}/pngs/{p}.png'
        if os.path.exists(algo1_fname) and os.path.exists(algo2_fname) and os.path.exists(algo3_fname):

            stcols[0].image(algo1_fname)
            stcols[1].image(algo2_fname)
            stcols[2].image(algo3_fname)
    'No more file pairs found'
