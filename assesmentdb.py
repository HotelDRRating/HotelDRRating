import pymysql as psql
__dbname = "hotelDRRating"
def create_table():
    conn = psql.connect(host='localhost',user='root',password='',database=__dbname)
    try:
        with conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS assessment(
                _id INTEGER PRIMARY KEY AUTO_INCREMENT,
                _hotelName TEXT NOT NULL,
                _hotelType TEXT NOT NULL,
                _hotelRate INTEGER NOT NULL,
                _hotelOwner TEXT NOT NULL,
                _hotelAffiliation TEXT NOT NULL,
                _hotelYrs TEXT NOT NULL,
                _hotelAssessorName TEXT NOT NULL,
                _hotelAssessorDesignation TEXT NOT NULL,
                _hotelAssessorContact TEXT NOT NULL,
                _hotelAssessorEmail TEXT NOT NULL,
                _hotelAssessmentDate DATE NOT NULL,
                _hotelGeoEarthquakeLikely TEXT NOT NULL,
                _hotelGeoEarthquakeImpact TEXT NOT NULL,
                _hotelGeoLiquefactionLikely TEXT NOT NULL,
                _hotelGeoLiquefactionImpact TEXT NOT NULL,
                _hotelGeoGroundRuptureLikely TEXT NOT NULL,
                _hotelGeoGroundRuptureImpact TEXT NOT NULL,
                _hotelGeoTsunamiLikely TEXT NOT NULL,
                _hotelGeoTsunamiImpact TEXT NOT NULL,
                _hotelGeoVolcanicLikely TEXT NOT NULL,
                _hotelGeoVolcanicImpact TEXT NOT NULL,
                _hotelGeoLandslideLikely TEXT NOT NULL,
                _hotelGeoLandslideImpact TEXT NOT NULL,
                _hotelHMCycloneLikely TEXT NOT NULL,
                _hotelHMCycloneImpact TEXT NOT NULL,
                _hotelHMFloodLikely TEXT NOT NULL,
                _hotelHMFloodImpact TEXT NOT NULL,
                _hotelHMStormSLikely TEXT NOT NULL,
                _hotelHMStormSImpact TEXT NOT NULL,
                _hotelMMTerrorismLikely TEXT NOT NULL,
                _hotelMMTerrorismImpact TEXT NOT NULL,
                _hotelMMCivilDLikely TEXT NOT NULL,
                _hotelMMCivilDImpact TEXT NOT NULL,
                _hotelMMCyberAttLikely TEXT NOT NULL,
                _hotelMMCyberAttImpact TEXT NOT NULL,
                _hotelMMHazardMatLikely TEXT NOT NULL,
                _hotelMMHazardMatImpact TEXT NOT NULL,
                _hotelMMChemSpillLikely TEXT NOT NULL,
                _hotelMMChemSpillImpact TEXT NOT NULL,
                _hotelMMOilSpillLikely TEXT NOT NULL,
                _hotelMMOilSpillImpact TEXT NOT NULL,
                _hotelMMGasLeakLikely TEXT NOT NULL,
                _hotelMMGasLeakImpact TEXT NOT NULL,
                _hotelAssetArtwork INTEGER NOT NULL,
                _hotelAssetPaintingCount INTEGER NOT NULL,
                _hotelAssetSculptureCount INTEGER NOT NULL,
                _hotelAssetBuildingCount INTEGER NOT NULL,
                _hotelAssetGeneratorCount INTEGER NOT NULL,
                _hotelAssetToolCount INTEGER NOT NULL,
                _hotelAssetTesterCount INTEGER NOT NULL,
                _hotelAssetDesktopCount INTEGER NOT NULL,
                _hotelAssetLaptopCount INTEGER NOT NULL,
                _hotelAssetPrinterCount INTEGER NOT NULL,
                _hotelAssetNetSwitchCount INTEGER NOT NULL,
                _hotelAssetRouterCount INTEGER NOT NULL,
                _hotelAssetStoveCount INTEGER NOT NULL,
                _hotelAssetOvenCount INTEGER NOT NULL,
                _hotelAssetRefCount INTEGER NOT NULL,
                _hotelAssetFreezerCount INTEGER NOT NULL,
                _hotelAssetChairCount INTEGER NOT NULL,
                _hotelAssetTableCount INTEGER NOT NULL,
                _hotelAssetFileCabCount INTEGER NOT NULL,
                _hotelAssetXeroxCount INTEGER NOT NULL,
                _hotelAssetBroomCount INTEGER NOT NULL,
                _hotelAssetDustPansCount INTEGER NOT NULL,
                _hotelAssetVaccCount INTEGER NOT NULL,
                _hotelAssetFloorPolCount INTEGER NOT NULL,
                _hotelAssetCCTVCount INTEGER NOT NULL,
                _hotelAssetSecAlarmCount INTEGER NOT NULL,
                _hotelAssetSecPersonCount INTEGER NOT NULL,
                _hotelAssetSecVehicleCount INTEGER NOT NULL,
                _hotelAssetEmployeesCount INTEGER NOT NULL,
                _hotelAssetSubConEmployeesCount TEXT NOT NULL,
                _hotelAssetSupplierCount TEXT NOT NULL,
                _hotelHasAssetProtection TEXT NOT NULL,
                _hotelHasRiskManagementPlan TEXT NOT NULL,
                _hotelHasBusinessContPlan TEXT NOT NULL,
                _hotelHasRiskReductionPlan TEXT NOT NULL,
                _hotelHasCrisisManagementPlan TEXT NOT NULL,
                _hotelHasOpportunityManagementPlan TEXT NOT NULL,
                _hotelHasRiskCommunicationPlan TEXT NOT NULL,
                _hotelHasCrisisCommunicationPlan TEXT NOT NULL,
                _emailused TEXT NOT NULL
                )"""
            cursor.execute(sql)
            conn.commit()
    finally:
        conn.close()
def insert(hotelname,hoteltype,hotelrate,hotelowner,hotelaffiliation,hotelyears,hotelassessorname,hotelassessordesignation,hotelassessorcontact,hotelassessmentemail,hotelassessmentdate,earthquakelikely,earthquakeimpact,liquefactionlikely,liquefactionimpact,grupturelikely,gruptureimpact,tsunamilikely,tsunamiimpact,volcaniclikely,volcanicimpact,landslidelikely,landslideimpact,cyclonelikely,cycloneimpact,floodlikely,floodimpact,stormlikely,stormimpact,terrorismlikely,terrorismimpact,civildistlikely,civildistimpact,cyberattlikely,cyberattimpact,hazardmatlikely,hazardmatimpact,chemspilllikely,chemspillimpact,oilspilllikely,oilspillimpact,gasleaklikely,gasleakimpact,artwork,painting,sculpture,buildings,generator,tool,tester,desktop,laptop,printer,netswitch,router,stove,oven,ref,freezer,chair,table,filecab,xerox,broom,dustpan,vaccume,floorpolish,cctv,secalarm,secperson,secvehicle,employeescount,subcontractor,supplier,assetprot,riskmgmt,bcp,risk,crisis,opportunity,riskcomm,crisiscomm,email):
    conn = psql.connect(host='localhost',user='root',password='',database=__dbname)
    try:
        with conn.cursor() as cursor:
            sql = f"""
            INSERT INTO assessment(_hotelName,_hotelType,_hotelRate,_hotelOwner,_hotelAffiliation,_hotelYrs,_hotelAssessorName,_hotelAssessorDesignation,_hotelAssessorContact,_hotelAssessorEmail,_hotelAssessmentDate,_hotelGeoEarthquakeLikely,_hotelGeoEarthquakeImpact,_hotelGeoLiquefactionLikely,_hotelGeoLiquefactionImpact,_hotelGeoGroundRuptureLikely,_hotelGeoGroundRuptureImpact,_hotelGeoTsunamiLikely,_hotelGeoTsunamiImpact,_hotelGeoVolcanicLikely,_hotelGeoVolcanicImpact,_hotelGeoLandslideLikely,_hotelGeoLandslideImpact,_hotelHMCycloneLikely,_hotelHMCycloneImpact,_hotelHMFloodLikely,_hotelHMFloodImpact,_hotelHMStormSLikely,_hotelHMStormSImpact,_hotelHMStormSImpact,_hotelMMTerrorismImpact,_hotelMMCivilDLikely,_hotelMMCivilDImpact,_hotelMMCyberAttLikely,_hotelMMCyberAttImpact,_hotelMMHazardMatLikely,_hotelMMHazardMatImpact,_hotelMMChemSpillLikely,_hotelMMChemSpillImpact,_hotelMMOilSpillLikely,_hotelMMOilSpillImpact,_hotelMMGasLeakLikely,_hotelMMGasLeakImpact,_hotelAssetArtwork,_hotelAssetPaintingCount,_hotelAssetSculptureCount,_hotelAssetBuildingCount,_hotelAssetGeneratorCount,_hotelAssetToolCount,_hotelAssetTesterCount,_hotelAssetDesktopCount,_hotelAssetLaptopCount,_hotelAssetPrinterCount,_hotelAssetNetSwitchCount,_hotelAssetRouterCount,_hotelAssetStoveCount,_hotelAssetOvenCount,_hotelAssetRefCountm,_hotelAssetFreezerCount,_hotelAssetChairCount,_hotelAssetTableCount,_hotelAssetFileCabCount,_hotelAssetXeroxCount,_hotelAssetBroomCount,_hotelAssetDustPansCount,_hotelAssetVaccCount,_hotelAssetFloorPolCount,_hotelAssetCCTVCount,_hotelAssetSecAlarmCount,_hotelAssetSecAlarmCount,_hotelAssetSecVehicleCount,_hotelAssetEmployeesCount,_hotelAssetSubConEmployeesCount,_hotelAssetSupplierCount,_hotelHasAssetProtection,_hotelHasRiskManagementPlan,_hotelHasBusinessContPlan,_hotelHasRiskReductionPlan,_hotelHasCrisisManagementPlan,_hotelHasOpportunityManagementPlan,_hotelHasRiskCommunicationPlan,_hotelHasCrisisCommunicationPlan)
            VALUES('{hotelname}','{hoteltype}',{hotelrate},'{hotelowner}','{hotelaffiliation}','{hotelyears}','{hotelassessorname}','{hotelassessordesignation}','{hotelassessorcontact}','{hotelassessmentemail}','{hotelassessmentdate}','{earthquakelikely}','{earthquakeimpact}','{liquefactionlikely}','{liquefactionimpact}','{grupturelikely}','{gruptureimpact}','{tsunamilikely}','{tsunamiimpact}','{volcaniclikely}','{volcanicimpact}','{landslidelikely}','{landslideimpact}','{cyclonelikely}','{cycloneimpact}','{floodlikely}','{floodimpact}','{stormlikely}','{stormimpact}','{terrorismlikely}','{terrorismimpact}','{civildistlikely}','{civildistimpact}','{cyberattlikely}','{cyberattimpact}','{hazardmatlikely}','{hazardmatimpact}','{chemspilllikely}','{chemspillimpact}','{oilspilllikely}','{oilspillimpact}','{gasleaklikely}','{gasleakimpact}',{artwork},{painting},{sculpture},{buildings},{generator},{tool},{tester},{desktop},{laptop},{printer},{netswitch},{router},{stove},{oven},{ref},{freezer},{chair},{table},{filecab},{xerox},{broom},{dustpan},{vaccume},{floorpolish},{cctv},{secalarm},{secperson},{secvehicle},{employeescount},'{subcontractor}','{supplier}','{assetprot}','{riskmgmt}','{bcp}','{risk}','{crisis}','{opportunity}','{riskcomm}','{crisiscomm}','{email}')
            """
            cursor.execute(sql)
    finally:
        conn.close()