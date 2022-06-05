# Open Bus Stride Data Model

![Database Schema Diagram](dbschema.png)

### gtfs_route

#### id

#### date

#### line_ref

#### operator_ref

#### route_short_name

#### route_long_name

#### route_mkt

#### route_direction

#### route_alternative

#### agency_name

#### route_type

### gtfs_stop

#### id

#### date

#### code

#### lat

#### lon

#### name

#### city

### gtfs_stop_mot_id

#### id

#### gtfs_stop_id

#### mot_id

### siri_snapshot

#### id

#### snapshot_id

#### etl_status

#### etl_start_time

#### etl_end_time

#### error

#### num_successful_parse_vehicle_locations

#### num_failed_parse_vehicle_locations

#### num_added_siri_rides

#### num_added_siri_ride_stops

#### num_added_siri_routes

#### num_added_siri_stops

#### last_heartbeat

#### created_by

### gtfs_ride

#### id

#### gtfs_route_id

#### journey_ref

#### first_gtfs_ride_stop_id

#### last_gtfs_ride_stop_id

#### start_time

#### end_time

### gtfs_ride_stop

#### id

#### gtfs_stop_id

#### gtfs_ride_id

#### arrival_time

#### departure_time

#### stop_sequence

#### pickup_type

#### drop_off_type

#### shape_dist_traveled

### siri_ride

#### id

#### siri_route_id

#### journey_ref

#### scheduled_start_time

#### vehicle_ref

#### updated_first_last_vehicle_locations

#### first_vehicle_location_id

#### last_vehicle_location_id

#### updated_duration_minutes

#### duration_minutes

#### journey_gtfs_ride_id

#### route_gtfs_ride_id

#### gtfs_ride_id

### siri_ride_stop

A stop along a ride received from the SIRI data.
All SIRI Vehicle locations are related to this object on [[siri_vehicle_location.siri_ride_stop_id]]

#### id

#### siri_stop_id

#### siri_ride_id

#### order

The order of this stop along the ride, first stop is 0

#### gtfs_stop_id

The related [[gtfs_stop]]

#### nearest_siri_vehicle_location_id

### siri_route

A Bus route which was received from the SIRI data.
Multiple rides can occur on a route, these are available in [[siri_ride]]
and related by [[siri_ride.siri_route_id]]

#### id

#### line_ref

In combination with the [[operator_ref]] - uniquely identifies the route and relates to the GTFS identifiers

#### operator_ref

In combination with the [[line_ref]] - uniquely identifies the route and relates to the GTFS identifiers

### siri_stop

#### id

#### code

### siri_vehicle_location

#### id

#### siri_snapshot_id

#### siri_ride_stop_id

#### recorded_at_time

#### lon

#### lat

#### bearing

#### velocity

#### distance_from_journey_start

#### distance_from_siri_ride_stop_meters

