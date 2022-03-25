import streamlit as st
import glob
import os

st.set_page_config(layout='wide')

display_type = st.selectbox('display_type', ['naive', 'naive vs beam'])

dirs = glob.glob('data/*')
dirs = list(filter(os.path.isdir, dirs))


if display_type == 'naive':
    percentiles = [10, 25, 50]
    stcols = st.columns(len(percentiles))

    for d in dirs:
        for i, p in enumerate(percentiles):
            fname = d + f'/naive/pngs/{p}.png'
            stcols[i].image(fname)
    'No more files found'

elif display_type == 'naive vs beam':
    p = st.selectbox('percent of lines', [10, 25, 50], 2)
    stcols = st.columns(2)
    stcols[0].header('Naive')
    stcols[1].header('Beam')

    for d in dirs:
        naive_fname = d + f'/naive/pngs/{p}.png'
        beam_fname = d + f'/beam/pngs/{p}.png'

        if os.path.exists(beam_fname) and os.path.exists(naive_fname):

            stcols[0].image(naive_fname)
            stcols[1].image(beam_fname)

    'No more file pairs found'
