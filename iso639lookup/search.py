import importlib.resources
import pandas as pd
import json


class ISO639Lookup:
    def __init__(self, data_filename="iso-info.csv"):
       with importlib.resources.files("iso639lookup.resources").joinpath(data_filename).open("r", encoding="utf-8") as f:
            self.data = pd.read_csv(f, keep_default_na=False)
    def isoRowFind(self, code):
       
        return self.data[
            (self.data['part3'] == code) | 
            (self.data['part2b'] == code) | 
            (self.data['part2t'] == code) | 
            (self.data['part1'] == code)
            ]
    def get_iso_part1(self, code):
        result = self.isoRowFind(code)

        if result.empty:
            return None
        
        if pd.isna(result["part1"].iloc[0]):
            return None
        
        return result["part1"].iloc[0]
    
    def get_iso_part2t(self, code):
        result = self.isoRowFind(code)


        if result.empty:
            return None
        
        if pd.isna(result["Part2t"].iloc[0]):
            return None
        return result["part2t"].iloc[0]
    def get_iso_part2b(self, code):
        result = self.isoRowFind(code)

        if result.empty:
            return None
        
        if pd.isna(result["part2b"].iloc[0]):
            return None
        return result["part2b"].iloc[0]
    def get_iso_part3(self, code):
        result = self.isoRowFind(code)

        if result.empty:
            return None
        
        if pd.isna(result["part3"].iloc[0]):
            return None
        return result["part3"].iloc[0]
    
    def iso_lookup(self, code):
        result = self.isoRowFind(code)
        return json.loads(result.to_json(orient="records", index=False))[0]
    