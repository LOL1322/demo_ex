from server.routers import expeditions, firms, fossils, personnel, positions, users

routers = (expeditions.expeditions_router, firms.firms_router, fossils.fossils_router, personnel.personnel_router, positions.positions_router, users.users_router)

