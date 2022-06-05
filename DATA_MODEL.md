# Open Bus Stride Data Model

![Database Schema Diagram](dbschema.png)

### gtfs_route

#### gtfs_route.id

#### gtfs_route.date

#### gtfs_route.line_ref

#### gtfs_route.operator_ref

#### gtfs_route.route_short_name

#### gtfs_route.route_long_name

#### gtfs_route.route_mkt

#### gtfs_route.route_direction

#### gtfs_route.route_alternative

#### gtfs_route.agency_name

#### gtfs_route.route_type

### gtfs_stop

#### gtfs_stop.id

#### gtfs_stop.date

#### gtfs_stop.code

#### gtfs_stop.lat

#### gtfs_stop.lon

#### gtfs_stop.name

#### gtfs_stop.city

### gtfs_stop_mot_id

#### gtfs_stop_mot_id.id

#### gtfs_stop_mot_id.gtfs_stop_id

#### gtfs_stop_mot_id.mot_id

### siri_snapshot

#### siri_snapshot.id

#### siri_snapshot.snapshot_id

#### siri_snapshot.etl_status

#### siri_snapshot.etl_start_time

#### siri_snapshot.etl_end_time

#### siri_snapshot.error

#### siri_snapshot.num_successful_parse_vehicle_locations

#### siri_snapshot.num_failed_parse_vehicle_locations

#### siri_snapshot.num_added_siri_rides

#### siri_snapshot.num_added_siri_ride_stops

#### siri_snapshot.num_added_siri_routes

#### siri_snapshot.num_added_siri_stops

#### siri_snapshot.last_heartbeat

#### siri_snapshot.created_by

### gtfs_ride

#### gtfs_ride.id

#### gtfs_ride.gtfs_route_id

#### gtfs_ride.journey_ref

#### gtfs_ride.first_gtfs_ride_stop_id

#### gtfs_ride.last_gtfs_ride_stop_id

#### gtfs_ride.start_time

#### gtfs_ride.end_time

### gtfs_ride_stop

#### gtfs_ride_stop.id

#### gtfs_ride_stop.gtfs_stop_id

#### gtfs_ride_stop.gtfs_ride_id

#### gtfs_ride_stop.arrival_time

#### gtfs_ride_stop.departure_time

#### gtfs_ride_stop.stop_sequence

#### gtfs_ride_stop.pickup_type

#### gtfs_ride_stop.drop_off_type

#### gtfs_ride_stop.shape_dist_traveled

### siri_ride

#### siri_ride.id

#### siri_ride.siri_route_id

#### siri_ride.journey_ref

#### siri_ride.scheduled_start_time

#### siri_ride.vehicle_ref

#### siri_ride.updated_first_last_vehicle_locations

#### siri_ride.first_vehicle_location_id

#### siri_ride.last_vehicle_location_id

#### siri_ride.updated_duration_minutes

#### siri_ride.duration_minutes

#### siri_ride.journey_gtfs_ride_id

#### siri_ride.route_gtfs_ride_id

#### siri_ride.gtfs_ride_id

### siri_ride_stop

A stop along a ride received from the SIRI data.
All SIRI Vehicle locations are related to this object on [siri_vehicle_location.siri_ride_stop_id](https://github.com/hasadna/open-bus-stride-db/blob/main/DATA_MODEL.md#siri_vehicle_locationsiri_ride_stop_id)

#### siri_ride_stop.id

#### siri_ride_stop.siri_stop_id

#### siri_ride_stop.siri_ride_id

#### siri_ride_stop.order

The order of this stop along the ride, first stop is 0

#### siri_ride_stop.gtfs_stop_id

The related [gtfs_stop](https://github.com/hasadna/open-bus-stride-db/blob/main/DATA_MODEL.md#gtfs_stop)

#### siri_ride_stop.nearest_siri_vehicle_location_id

### siri_route

A Bus route which was received from the SIRI data.
Multiple rides can occur on a route, these are available in [siri_ride](https://github.com/hasadna/open-bus-stride-db/blob/main/DATA_MODEL.md#siri_ride)
and related by [siri_ride.siri_route_id](https://github.com/hasadna/open-bus-stride-db/blob/main/DATA_MODEL.md#siri_ridesiri_route_id)

#### siri_route.id

#### siri_route.line_ref

In combination with the [operator_ref](https://github.com/hasadna/open-bus-stride-db/blob/main/DATA_MODEL.md#siri_routeoperator_ref) - uniquely identifies the route and relates to the GTFS identifiers

#### siri_route.operator_ref

In combination with the [line_ref](https://github.com/hasadna/open-bus-stride-db/blob/main/DATA_MODEL.md#siri_routeline_ref) - uniquely identifies the route and relates to the GTFS identifiers

### siri_stop

#### siri_stop.id

#### siri_stop.code

### siri_vehicle_location

#### siri_vehicle_location.id

#### siri_vehicle_location.siri_snapshot_id

#### siri_vehicle_location.siri_ride_stop_id

#### siri_vehicle_location.recorded_at_time

#### siri_vehicle_location.lon

#### siri_vehicle_location.lat

#### siri_vehicle_location.bearing

#### siri_vehicle_location.velocity

#### siri_vehicle_location.distance_from_journey_start

#### siri_vehicle_location.distance_from_siri_ride_stop_meters

