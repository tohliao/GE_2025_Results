import folium
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium
from branca.element import Element

APP_TITLE = '🗳️GE2025 Results'
APP_SUB_TITLE = 'Source: Elections Department Singapore (ELD). Image/Logo Credits from Wikipedia'

# CSS to remove focus outline on tooltip click
css = """
    <style>
    .leaflet-interactive:focus {
        outline: none !important;
        box-shadow: none !important;
    }
    </style>
"""

# Elected Seats Legend
legend_html = """
       <div style="
           position: fixed;
           right: 10px;
           top: 10px;
           background-color: rgba(255, 255, 255, 0.85);
           padding:10px;
           border:1px solid grey;
           z-index:9999;
           font-size:12px;
           color: black;
           ">
           <b>Elected Seats:</b><br>
            <div style="display: flex; align-items: center; margin-bottom: 5px;">
                <div style="background-color: rgba(255, 0, 0, 0.45); width: 12px; height: 12px; display: inline-block; margin-right: 5px;"></div>
                    People's Action Party (PAP)
            </div>
            <div style="display: flex; align-items: center;">
                <div style="background-color: rgba(100, 100, 255, 0.45); width: 12px; height: 12px; display: inline-block; margin-right: 5px;"></div>
                    Workers' Party (WP)
            </div>
       </div>
   """

def main():
    st.set_page_config(page_title=APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)

    # Load Data
    df = pd.read_csv('GE2025_MP Data/GE2025_Results.csv')
    da = pd.read_csv('GE2025_MP Data/GE2025_Namelist.csv')
    df = df.replace('\n', '', regex=True)
    da = da.replace('\n', '', regex=True)

    constituency_type = 'Type'

    grc_count = df.loc[df[constituency_type] == 2].shape[0]
    smc_count = df.loc[df[constituency_type] == 1].shape[0]

    # Metric Data
    st.write("")
    col1,col2 = st.columns([4,1])

    with col1:
        st.metric('Total GRC Count', '{:,}'.format(grc_count))
    with col2:
        st.metric('Total SMC Count', '{:,}'.format(smc_count))

    #Add Disclaimer
    st.caption("Refresh the page if you encounter excess whitespace between the map and electoral results.")

    # Define color mapping per party
    color_map = {
        'PAP': '#FF0000',           # PAP
        'WP': '#6464ff',          # WP
        'PSP': '#ff3232',        # PSP
        'SDP': '#c81414',         # SDP
        'RDU': '#000096',        # RDU
        'SDA': '#00ff00',          # SDA
        'SPP': '#966496',        # SPP
        'NSP': '#ff783c',         # NSP
        'PAR': '#643264',          # PAR
        'PPP': '#c832c8',      # PPP
        'SUP': '#c8c800',         # SUP
        'IndependentRM': '#646464',  # Independent for RADIN MAS SMC
        'IndependentMB': '#646464' # Independent for MOUNTBATTEN SMC
    }

    # Create Folium map
    m = folium.Map(location=[1.3521, 103.8198], zoom_start=11)

    # Add HTML Legend to map
    m.get_root().html.add_child(Element(legend_html))

    # Add the CSS to the map
    m.get_root().html.add_child(Element(css))

    # Edit map colouring
    def style_function(feature):
        constituency = feature["properties"]["ED_DESC_FU"]
        incumbent = df.loc[df["Constituency"] == constituency, "Incumbent"].values[0]
        color = color_map.get(incumbent, 'red')
        return {
            "fillColor": color,
            "color": "black",
            "weight": 2,
            "fillOpacity": 0.4,
            "clickHighlight": True
        }

    # Add GeoJSON layer with style function
    folium.GeoJson(
        'GE2025_MP Data/ElectoralBoundary2025GEOJSON.geojson',
        name="Electoral Boundaries",
        style_function=style_function,
        highlight_function=lambda feat: {'fillColor': '#c8c8c8'},
        tooltip=folium.GeoJsonTooltip(
            fields=["ED_DESC_FU"],
            aliases=[""]
        ),
    ).add_to(m)

    # Display the map
    st_map = st_folium(m, width=800, height=500)

    # Array to loop for each contesting party
    parties = ('PAP', 'WP', 'PSP', 'SDP', 'RDU', 'SDA', 'SPP', 'NSP', 'PAR', 'PPP', 'SUP', 'IndependentRM', 'IndependentMB')

    # When user click on a Constituency
    if st_map['last_object_clicked_tooltip']:
        selected_constituency = st_map['last_object_clicked_tooltip']
        st.subheader(selected_constituency, divider=True)
        sort_result = {}
        namelist = {}

        # Party Official Names (Long Form)
        official_name = {
            'PAP': "People's Action Party (PAP)",  # PAP
            'WP': "The Workers' Party (WP)",  # WP
            'PSP': 'Progress Singapore Party (PSP)',  # PSP
            'SDP': 'Singapore Democratic Party (SDP)',  # SDP
            'RDU': 'Red Dot United (RDU)',  # RDU
            'SDA': 'Singapore Democratic Alliance (SDA)',  # SDA
            'SPP': "Singapore People's Party (SPP)",  # SPP
            'NSP': 'National Solidarity Party (NSP)',  # NSP
            'PAR': "People's Alliance for Reform (PAR)",  # PAR
            'PPP': "People's Power Party (PPP)",  # PPP
            'SUP': 'Singapore United Party (SUP)',  # SUP
            'IndependentRM': 'Independent',  # Independent
            'IndependentMB': 'Independent' # Independent
        }

        # Party Official Logos (link to assets)
        party_logo = {
            'PAP': 'Images/PAP_Logo.png',  # PAP
            'WP': "Images/WP_Logo.png",  # WP
            'PSP': 'Images/PSP_Logo.png',  # PSP
            'SDP': 'Images/SDP_Logo.png',  # SDP
            'RDU': 'Images/RDU_Logo.png',  # RDU
            'SDA': 'Images/SDA_Logo.png',  # SDA
            'SPP': "Images/SPP_Logo.png",  # SPP
            'NSP': 'Images/NSP_Logo.png',  # NSP
            'PAR': "Images/PAR_Logo.png",  # PAR
            'PPP': "Images/PPP_Logo.png",  # PPP
            'SUP': 'Images/SUP_Logo.png',  # SUP
            'IndependentRM': 'Images/IndependentRM_Logo.png', # Leave Blank
            'IndependentMB': 'Images/IndependentMB_Logo.png'  # Leave Blank
        }

        # if selected_constituency:
        constituency_row = df[df['Constituency'] == selected_constituency.strip().replace('\n', '')].iloc[0]
        candidates = da[da['Constituency'] == selected_constituency.strip().replace('\n', '')].iloc[0]

        def capture_result(sort_result, key, value):
            sort_result[key] = value
            final_result = dict(sorted(sort_result.items(), key=lambda item: item[1], reverse=True))
            return final_result

        def contested_candidates(namelist, key, name):
            namelist[key] = name
            return namelist

        for party in parties:
            key = party
            value = constituency_row[party]
            name = candidates[party]
            sort_result = capture_result(sort_result, key, value)
            namelist = contested_candidates(namelist, key, name)

        for key, value in sort_result.items():
            if key in official_name:
                party_full_name = official_name[key]
                name = candidates[key]
                st.write("")
            if value != 0.0 and value != 1.0:
                if value >= 0.5:
                    st.image(party_logo[key])
                    st.markdown(f"**:green[{party_full_name}: {round(value * 100,2)}%] :green-badge[:material/check: Elected]**")
                elif value < 0.5:
                    st.image(party_logo[key])
                    st.write(f'{party_full_name}: {round(value * 100,2)}%')
                st.caption(name)
                st.progress(value)
                st.write("")
                st.divider()
            elif value == 1.0:
                st.image(party_logo[key])
                st.markdown(f"**:green[{party_full_name}: Walkover]**")
                st.caption(name)
                st.progress(value)
                st.write("")
                st.divider()
    else:
        st.subheader('Click Constituency for Information')


if __name__ == '__main__':
    main()
