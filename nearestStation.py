import sqlite3 as db


def RunLookup(lng, lat):
    try:
        conn = db.connect('amtrakStations.sqlite')
        conn.enable_load_extension(True);
        cmd = "select load_extension('mod_spatialite.dll')"
        cur = conn.cursor()
        cur.execute(cmd)

    except Exception as e:
        raise e

    # Query using ST_Distance function with the ellipsoid argument
    #and it only works with with Spatialite 4.0.1
    cmd = "select stnname, ST_Distance(geometry,GeomFromText('"
    cmd += "POINT(%s %s)'" % (str(lng), str(lat))
    cmd += "), 1) as distance from stationLayer order by distance ASC limit 1"

    cur.execute(cmd)
    row = cur.fetchone()
    conn.close()

    print(str(row))
    storeId = row[0]
    distMeters = row[1]
    distMeters = "{0:.2f}".format(distMeters)

    resultList = [storeId, distMeters]

    return resultList


def main():
    resultList = RunLookup(-105.166667, 39.933333)
    print("found {_cnt} results".format(_cnt=str(len(resultList))))
    storeId = resultList[0]
    distMeters = resultList[1]

    print "the Amtrak station in %s is about %s meters away" % (storeId, distMeters)

if __name__ == "__main__":
    main()
