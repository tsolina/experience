from experience.system import AnyObject
from experience.cat_gsm_interfaces import HybridShape3DCurveOffset
from experience.cat_gsm_interfaces import HybridShapeAffinity
from experience.cat_gsm_interfaces import HybridShapeAssemble
from experience.cat_gsm_interfaces import HybridShapeAxisLine
from experience.cat_gsm_interfaces import HybridShapeAxisToAxis
from experience.cat_gsm_interfaces import HybridShapeBlend
from experience.cat_gsm_interfaces import HybridShapeBoundary
from experience.cat_gsm_interfaces import HybridShapeBump
from experience.cat_gsm_interfaces import HybridShapeCircle2PointsRad
from experience.cat_gsm_interfaces import HybridShapeCircle3Points
from experience.cat_gsm_interfaces import HybridShapeCircleBitangentPoint
from experience.cat_gsm_interfaces import HybridShapeCircleBitangentRadius
from experience.cat_gsm_interfaces import HybridShapeCircleCenterAxis
from experience.cat_gsm_interfaces import HybridShapeCircleCenterTangent
from experience.cat_gsm_interfaces import HybridShapeCircleCtrPt
from experience.cat_gsm_interfaces import HybridShapeCircleCtrRad
from experience.cat_gsm_interfaces import HybridShapeCircleExplicit
from experience.cat_gsm_interfaces import HybridShapeCircleTritangent
from experience.cat_gsm_interfaces import HybridShapeCombine
from experience.cat_gsm_interfaces import HybridShapeConic
from experience.cat_gsm_interfaces import HybridShapeConnect
from experience.cat_gsm_interfaces import HybridShapeCorner
from experience.cat_gsm_interfaces import HybridShapeCurveExplicit
from experience.cat_gsm_interfaces import HybridShapeCurvePar
from experience.cat_gsm_interfaces import HybridShapeCurveSmooth
from experience.cat_gsm_interfaces import HybridShapeCylinder
from experience.cat_gsm_interfaces import HybridShapeDevelop
from experience.cat_gsm_interfaces import HybridShapeDirection
from experience.cat_gsm_interfaces import HybridShapeExtract
from experience.cat_gsm_interfaces import HybridShapeExtractMulti
from experience.cat_gsm_interfaces import HybridShapeExtrapol
from experience.cat_gsm_interfaces import HybridShapeExtremum
from experience.cat_gsm_interfaces import HybridShapeExtremumPolar
from experience.cat_gsm_interfaces import HybridShapeExtrude
from experience.cat_gsm_interfaces import HybridShapeFill
from experience.cat_gsm_interfaces import HybridShapeFilletBiTangent
from experience.cat_gsm_interfaces import HybridShapeFilletTriTangent
from experience.cat_gsm_interfaces import HybridShapeHealing
from experience.cat_gsm_interfaces import HybridShapeHelix
from experience.cat_gsm_interfaces import HybridShapeIntegratedLaw
from experience.cat_gsm_interfaces import HybridShapeIntersection
from experience.cat_gsm_interfaces import HybridShapeInverse
from experience.cat_gsm_interfaces import HybridShapeLawDistProj
from experience.cat_gsm_interfaces import HybridShapeLineAngle
from experience.cat_gsm_interfaces import HybridShapeLineBiTangent
from experience.cat_gsm_interfaces import HybridShapeLineBisecting
from experience.cat_gsm_interfaces import HybridShapeLineExplicit
from experience.cat_gsm_interfaces import HybridShapeLineNormal
from experience.cat_gsm_interfaces import HybridShapeLinePtDir
from experience.cat_gsm_interfaces import HybridShapeLinePtPt
from experience.cat_gsm_interfaces import HybridShapeLineTangency
from experience.cat_gsm_interfaces import HybridShapeLoft
from experience.cat_gsm_interfaces import HybridShapeMidSurface
from experience.cat_gsm_interfaces import HybridShapeNear
from experience.cat_gsm_interfaces import HybridShapeOffset
from experience.cat_gsm_interfaces import HybridShapePlane1Curve
from experience.cat_gsm_interfaces import HybridShapePlane1Line1Pt
from experience.cat_gsm_interfaces import HybridShapePlane2Lines
from experience.cat_gsm_interfaces import HybridShapePlane3Points
from experience.cat_gsm_interfaces import HybridShapePlaneAngle
from experience.cat_gsm_interfaces import HybridShapePlaneBetween
from experience.cat_gsm_interfaces import HybridShapePlaneEquation
from experience.cat_gsm_interfaces import HybridShapePlaneExplicit
from experience.cat_gsm_interfaces import HybridShapePlaneMean
from experience.cat_gsm_interfaces import HybridShapePlaneNormal
from experience.cat_gsm_interfaces import HybridShapePlaneOffset
from experience.cat_gsm_interfaces import HybridShapePlaneOffsetPt
from experience.cat_gsm_interfaces import HybridShapePlaneTangent
from experience.cat_gsm_interfaces import HybridShapePointBetween
from experience.cat_gsm_interfaces import HybridShapePointCenter
from experience.cat_gsm_interfaces import HybridShapePointCoord
from experience.cat_gsm_interfaces import HybridShapePointExplicit
from experience.cat_gsm_interfaces import HybridShapePointOnCurve
from experience.cat_gsm_interfaces import HybridShapePointOnPlane
from experience.cat_gsm_interfaces import HybridShapePointOnSurface
from experience.cat_gsm_interfaces import HybridShapePointTangent
from experience.cat_gsm_interfaces import HybridShapePolyline
from experience.cat_gsm_interfaces import HybridShapePositionTransfo
from experience.cat_gsm_interfaces import HybridShapeProject
from experience.cat_gsm_interfaces import HybridShapeReflectLine
from experience.cat_gsm_interfaces import HybridShapeRevol
from experience.cat_gsm_interfaces import HybridShapeRotate
from experience.cat_gsm_interfaces import HybridShapeScaling
from experience.cat_gsm_interfaces import HybridShapeSection
from experience.cat_gsm_interfaces import HybridShapeSphere
from experience.cat_gsm_interfaces import HybridShapeSpine
from experience.cat_gsm_interfaces import HybridShapeSpiral
from experience.cat_gsm_interfaces import HybridShapeSpline
from experience.cat_gsm_interfaces import HybridShapeSplit
from experience.cat_gsm_interfaces import HybridShapeSurfaceExplicit
from experience.cat_gsm_interfaces import HybridShapeSweepCircle
from experience.cat_gsm_interfaces import HybridShapeSweepConic
from experience.cat_gsm_interfaces import HybridShapeSweepExplicit
from experience.cat_gsm_interfaces import HybridShapeSweepLine
from experience.cat_gsm_interfaces import HybridShapeSymmetry
from experience.cat_gsm_interfaces import HybridShapeTransfer
from experience.cat_gsm_interfaces import HybridShapeTranslate
from experience.cat_gsm_interfaces import HybridShapeTrim
from experience.cat_gsm_interfaces import HybridShapeUnfold
from experience.cat_gsm_interfaces import HybridShapeVolumeExplicit
from experience.cat_gsm_interfaces import HybridShapeWrapCurve
from experience.cat_gsm_interfaces import HybridShapeWrapSurface
from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import Factory
#from pycatia.scripts.vba import vba_nothing


class HybridShapeFactory(Factory):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Factory
                |                         HybridShapeFactory
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_factory = com

    def add_new_3d_corner(self, i_element1: Reference, i_element2: Reference, i_direction: HybridShapeDirection, i_radius: float, i_orientation1: int, i_orientation2: int, i_trim: bool ) -> HybridShapeCorner:
        return HybridShapeCorner( self.hybrid_shape_factory.AddNew3DCorner(i_element1._com, i_element2._com, i_direction._com, i_radius, i_orientation1, i_orientation2, i_trim ) )

    def add_new_3d_curve_offset( self, i_curve_to_offset: Reference, i_direction: HybridShapeDirection, i_offset: float, i_corner_radius: float, i_corner_tension: float ) -> HybridShape3DCurveOffset:
        return HybridShape3DCurveOffset( self.hybrid_shape_factory.AddNew3DCurveOffset( i_curve_to_offset._com, i_direction._com, i_offset, i_corner_radius, i_corner_tension ) )

    def add_new_affinity( self, i_element: Reference, i_x_ratio: float, i_y_ratio: float, i_z_ratio: float ) -> HybridShapeAffinity:
        return HybridShapeAffinity(self.hybrid_shape_factory.AddNewAffinity( i_element._com, i_x_ratio, i_y_ratio, i_z_ratio ) )

    def add_new_axis_line(self, i_element: Reference) -> HybridShapeAxisLine:
        return HybridShapeAxisLine(self.hybrid_shape_factory.AddNewAxisLine(i_element._com))

    def add_new_axis_to_axis( self, i_object: Reference, i_reference_axis: Reference, i_target_axis: Reference) -> HybridShapeAxisToAxis:
        return HybridShapeAxisToAxis( self.hybrid_shape_factory.AddNewAxisToAxis( i_object._com, i_reference_axis._com, i_target_axis._com ) )

    def add_new_blend(self) -> HybridShapeBlend:
        return HybridShapeBlend(self.hybrid_shape_factory.AddNewBlend())

    def add_new_boundary( self, i_initial_element: Reference, i_support: Reference, i_typede_propagation: int ) -> HybridShapeBoundary:
        return HybridShapeBoundary( self.hybrid_shape_factory.AddNewBoundary( i_initial_element._com, i_support._com, i_typede_propagation ) )

    def add_new_boundary_of_surface(self, surface: Reference) -> HybridShapeBoundary:
        return HybridShapeBoundary(self.hybrid_shape_factory.AddNewBoundaryOfSurface(surface._com))

    def add_new_bump(self, i_body_to_bump: Reference) -> HybridShapeBump:
        return HybridShapeBump(self.hybrid_shape_factory.AddNewBump(i_body_to_bump.com))

    def add_new_circle2_points_rad( self, i_point1: Reference, i_point2: Reference, i_support: Reference, i_geodesic: bool, i_radius: float, i_ori: int ) -> HybridShapeCircle2PointsRad:
        return HybridShapeCircle2PointsRad( self.hybrid_shape_factory.AddNewCircle2PointsRad( i_point1._com, i_point2._com, i_support._com, i_geodesic, i_radius, i_ori))

    def add_new_circle3_points( self, i_point1: Reference, i_point2: Reference, i_point3: Reference ) -> HybridShapeCircle3Points:
        return HybridShapeCircle3Points( self.hybrid_shape_factory.AddNewCircle3Points( i_point1._com, i_point2._com, i_point3._com ) )

    def add_new_circle_bitangent_point( self, i_curve1: Reference, i_curve2: Reference, i_point: Reference, i_support: Reference, i_ori1: int, i_ori2: int ) -> HybridShapeCircleBitangentPoint:
        return HybridShapeCircleBitangentPoint(self.hybrid_shape_factory.AddNewCircleBitangentPoint( i_curve1._com, i_curve2._com, i_point._com, i_support._com, i_ori1, i_ori2))

    def add_new_circle_bitangent_radius(self, i_curve1: Reference, i_curve2: Reference, i_support: Reference, i_radius: float, i_ori1: int, i_ori2: int) -> HybridShapeCircleBitangentRadius:
        return HybridShapeCircleBitangentRadius(self.hybrid_shape_factory.AddNewCircleBitangentRadius( i_curve1._com, i_curve2._com, i_support._com, i_radius, i_ori1, i_ori2))

    def add_new_circle_center_axis(self, i_axis: Reference, i_point: Reference, i_value: float, i_projection: bool) -> HybridShapeCircleCenterAxis:
        return HybridShapeCircleCenterAxis(self.hybrid_shape_factory.AddNewCircleCenterAxis(i_axis._com, i_point._com, i_value, i_projection))

    def add_new_circle_center_axis_with_angles(self, i_axis: Reference, i_point: Reference, i_value: float, i_projection: bool, i_start_angle: float, i_end_angle: float) -> HybridShapeCircleCenterAxis:
        return HybridShapeCircleCenterAxis(self.hybrid_shape_factory.AddNewCircleCenterAxisWithAngles( i_axis._com, i_point._com, i_value, i_projection, i_start_angle, i_end_angle))

    def add_new_circle_center_tangent(self, i_center_elem: Reference, i_tangent_curve: Reference, i_support: Reference, i_radius: float) -> HybridShapeCircleCenterTangent:
        return HybridShapeCircleCenterTangent(self.hybrid_shape_factory.AddNewCircleCenterTangent( i_center_elem._com, i_tangent_curve._com, i_support._com, i_radius))

    def add_new_circle_ctr_pt(self, i_center: Reference, i_crossing_point: Reference, i_support: Reference, i_geodesic: bool) -> HybridShapeCircleCtrPt:
        return HybridShapeCircleCtrPt(self.hybrid_shape_factory.AddNewCircleCtrPt(i_center._com, i_crossing_point._com, i_support._com, i_geodesic))

    def add_new_circle_ctr_pt_with_angles(self, i_center: Reference, i_crossing_point: Reference, i_support: Reference, i_geodesic: bool, i_start_angle: float, i_end_angle: float) -> HybridShapeCircleCtrPt:
        return HybridShapeCircleCtrPt( self.hybrid_shape_factory.AddNewCircleCtrPtWithAngles( i_center._com, i_crossing_point._com, i_support._com, i_geodesic, i_start_angle, i_end_angle))

    def add_new_circle_ctr_rad(self, i_center: Reference, i_support: Reference, i_geodesic: bool, i_radius: float) -> HybridShapeCircleCtrRad:
        return HybridShapeCircleCtrRad(self.hybrid_shape_factory.AddNewCircleCtrRad(i_center._com, i_support._com, i_geodesic, i_radius))

    def add_new_circle_ctr_rad_with_angles(self, i_center: Reference, i_support: Reference, i_geodesic: bool, i_radius: float, i_start_angle: float, i_end_angle: float) -> HybridShapeCircleCtrRad:
        return HybridShapeCircleCtrRad(self.hybrid_shape_factory.AddNewCircleCtrRadWithAngles(i_center._com, i_support._com, i_geodesic, i_radius, i_start_angle, i_end_angle))

    def add_new_circle_datum(self, i_object: Reference) -> HybridShapeCircleExplicit:
        return HybridShapeCircleExplicit(self.hybrid_shape_factory.AddNewCircleDatum(i_object._com))

    def add_new_circle_tritangent( self, i_curve1: Reference, i_curve2: Reference, i_curve3: Reference, i_support: Reference, i_ori1: int, i_ori2: int, i_ori3: int) -> HybridShapeCircleTritangent:
        return HybridShapeCircleTritangent(self.hybrid_shape_factory.AddNewCircleTritangent( i_curve1._com, i_curve2._com, i_curve3._com, i_support._com, i_ori1,i_ori2,i_ori3))

    def add_new_combine(self, i_first_curve: Reference, i_second_curve: Reference, i_nearest_solutions: int) -> HybridShapeCombine:
        return HybridShapeCombine(self.hybrid_shape_factory.AddNewCombine(i_first_curve._com, i_second_curve._com, i_nearest_solutions))

    def add_new_conic(self, i_support: Reference, i_starting_point: Reference, i_end_point: Reference) -> HybridShapeConic:
        return HybridShapeConic(self.hybrid_shape_factory.AddNewConic(i_support._com, i_starting_point._com, i_end_point._com))

    def add_new_conical_reflect_line_with_type(self, i_support: Reference, i_origin: Reference, i_angle: float, i_orientation_support: int, i_type: int ) -> HybridShapeReflectLine:
        return HybridShapeReflectLine(self.hybrid_shape_factory.AddNewConicalReflectLineWithType( i_support._com, i_origin._com, i_angle, i_orientation_support, i_type))

    def add_new_connect(self, i_curve1: Reference, i_point1: Reference, i_orient1: int, i_continuity1: int, i_tension1: float, i_curve2: Reference, i_point2: Reference, i_orient2: int, i_continuity2: int, i_tension2: float, trim: bool) -> HybridShapeConnect:
        return HybridShapeConnect(self.hybrid_shape_factory.AddNewConnect(
            i_curve1._com, i_point1._com, i_orient1, i_continuity1, i_tension1,
            i_curve2._com, i_point2._com, i_orient2, i_continuity2, i_tension2, trim))

    def add_new_corner(self, i_element1: Reference, i_element2: Reference, i_support: Reference, i_radius: float, i_orientation1: int, i_orientation2: int, i_trim: bool) -> HybridShapeCorner:
        return HybridShapeCorner(self.hybrid_shape_factory.AddNewCorner( i_element1._com, i_element2._com, i_support._com, i_radius, i_orientation1, i_orientation2, i_trim))

    def add_new_curve_datum(self, i_object: Reference) -> HybridShapeCurveExplicit:
        return HybridShapeCurveExplicit(self.hybrid_shape_factory.AddNewCurveDatum(i_object._com))

    def add_new_curve_par(self, curve: Reference, support: Reference, distance: float, invert_direction: bool, geodesic: bool) -> HybridShapeCurvePar:
        return HybridShapeCurvePar(self.hybrid_shape_factory.AddNewCurvePar(curve._com, support._com, distance, invert_direction, geodesic))

    def add_new_curve_smooth(self, ip_ia_curve: Reference) -> HybridShapeCurveSmooth:
        return HybridShapeCurveSmooth(self.hybrid_shape_factory.AddNewCurveSmooth(ip_ia_curve.com))

    def add_new_cylinder(self, i_center: Reference, i_radius: float, i_first_length: float, i_second_length: float, i_direction: HybridShapeDirection) -> HybridShapeCylinder:
        return HybridShapeCylinder(self.hybrid_shape_factory.AddNewCylinder(i_center._com, i_radius, i_first_length, i_second_length, i_direction._com))

    def add_new_datums(self, i_elem: Reference) -> tuple:
        # return self.hybrid_shape_factory.AddNewDatums(i_elem.com)
        from experience.mecmod_interfaces import HybridShape

        com_shapes = self.hybrid_shape_factory.AddNewDatums(i_elem.com)

        hybrid_shapes = []
        for com in com_shapes:
            hybrid_shapes.append(HybridShape(com))

        return tuple(hybrid_shapes)

    def add_new_develop(self, i_mode: int, i_to_develop: Reference, i_support: Reference) -> HybridShapeDevelop:
        return HybridShapeDevelop(self.hybrid_shape_factory.AddNewDevelop(i_mode, i_to_develop._com, i_support._com))

    def add_new_direction(self, i_element: Reference) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_factory.AddNewDirection(i_element._com))

    def add_new_direction_by_coord(self, i_x: float, i_y: float, i_z: float) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_factory.AddNewDirectionByCoord(i_x, i_y, i_z))

    def add_new_empty_rotate(self) -> HybridShapeRotate:
        return HybridShapeRotate(self.hybrid_shape_factory.AddNewEmptyRotate())

    def add_new_empty_translate(self) -> HybridShapeTranslate:
        return HybridShapeTranslate(self.hybrid_shape_factory.AddNewEmptyTranslate())

    def add_new_extract(self, element: Reference) -> HybridShapeExtract:
        return HybridShapeExtract(self.hybrid_shape_factory.AddNewExtract(element._com))

    def add_new_extract_multi(self, element: Reference) -> HybridShapeExtractMulti:
        return HybridShapeExtractMulti(self.hybrid_shape_factory.AddNewExtractMulti(element._com))

    def add_new_extrapol_length(self, i_boundary: Reference, i_to_extrapol: Reference, i_length: float) -> HybridShapeExtrapol:
        return HybridShapeExtrapol(self.hybrid_shape_factory.AddNewExtrapolLength(i_boundary.com, i_to_extrapol.com, i_length))

    def add_new_extrapol_until(self, i_boundary: Reference, i_to_extrapol: Reference, i_until: Reference) -> HybridShapeExtrapol:
        return HybridShapeExtrapol(self.hybrid_shape_factory.AddNewExtrapolUntil(i_boundary.com, i_to_extrapol.com, i_until.com))

    def add_new_extremum(self, i_objet: Reference, i_dir: HybridShapeDirection, i_min_max: int) -> HybridShapeExtremum:
        return HybridShapeExtremum(self.hybrid_shape_factory.AddNewExtremum(i_objet._com, i_dir._com, i_min_max))

    def add_new_extremum_polar(self, i_type: int, ip_ia_contour: Reference) -> HybridShapeExtremumPolar:
        return HybridShapeExtremumPolar(self.hybrid_shape_factory.AddNewExtremumPolar(i_type, ip_ia_contour._com))

    def add_new_extrude(self, i_object_to_extrude: Reference, i_offset_debut: float, i_offset_fin: float, i_direction: HybridShapeDirection) -> HybridShapeExtrude:
        return HybridShapeExtrude(self.hybrid_shape_factory.AddNewExtrude(i_object_to_extrude._com, i_offset_debut, i_offset_fin, i_direction._com))

    def add_new_fill(self) -> HybridShapeFill:
        return HybridShapeFill(self.hybrid_shape_factory.AddNewFill())

    def add_new_fillet_bi_tangent(self, i_element1: Reference, i_element2: Reference, i_radius: float, i_orientation1: int, i_orientation2: int, i_supports_trim_mode: int, i_ribbon_relimitation_mode: int) -> HybridShapeFilletBiTangent:
        return HybridShapeFilletBiTangent(self.hybrid_shape_factory.AddNewFilletBiTangent(i_element1._com, i_element2._com, i_radius, i_orientation1, i_orientation2, i_supports_trim_mode, i_ribbon_relimitation_mode))

    def add_new_fillet_tri_tangent(self, i_element1: Reference, i_element2: Reference, i_remove_elem: Reference, i_orientation1: int, i_orientation2: int, i_remove_orientation: int, i_supports_trim_mode: int, i_ribbon_relimitation_mode: int) -> HybridShapeFilletTriTangent:
        return HybridShapeFilletTriTangent(self.hybrid_shape_factory.AddNewFilletTriTangent(i_element1._com, i_element2._com, i_remove_elem._com, i_orientation1, i_orientation2, i_remove_orientation, i_supports_trim_mode, i_ribbon_relimitation_mode))

    def add_new_healing(self, i_body_toheal: Reference) -> HybridShapeHealing:
        return HybridShapeHealing(self.hybrid_shape_factory.AddNewHealing(i_body_toheal._com))

    def add_new_helix(self, i_axis: Reference, i_invert_axis: bool, i_starting_point: Reference, i_pitch: float, i_height: float, i_clockwise_revolution: bool, i_starting_angle: float, i_taper_angle: float, i_taper_outward: bool) -> HybridShapeHelix:
        return HybridShapeHelix(self.hybrid_shape_factory.AddNewHelix(i_axis._com, i_invert_axis, i_starting_point._com, i_pitch, i_height, i_clockwise_revolution, i_starting_angle, i_taper_angle, i_taper_outward))

    def add_new_hybrid_scaling(self, i_elem_to_scale: Reference, i_center: Reference, i_ratio: float) -> HybridShapeScaling:
        return HybridShapeScaling(self.hybrid_shape_factory.AddNewHybridScaling(i_elem_to_scale._com, i_center._com, i_ratio))

    def add_new_hybrid_split(self, i_element1: Reference, i_element2: Reference, i_orientation: int) -> HybridShapeSplit:
        return HybridShapeSplit(self.hybrid_shape_factory.AddNewHybridSplit(i_element1._com, i_element2._com, i_orientation))

    def add_new_hybrid_trim(self, i_element1: Reference, i_orientation1: int, i_element2: Reference, i_orientation2: int) -> HybridShapeTrim:
        return HybridShapeTrim(self.hybrid_shape_factory.AddNewHybridTrim(i_element1._com, i_orientation1, i_element2._com, i_orientation2))

    def add_new_integrated_law(self, i_type: int) -> HybridShapeIntegratedLaw:
        return HybridShapeIntegratedLaw(self.hybrid_shape_factory.AddNewIntegratedLaw(i_type))

    def add_new_intersection(self, i_object1: Reference, i_object2: Reference) -> HybridShapeIntersection:
        return HybridShapeIntersection(self.hybrid_shape_factory.AddNewIntersection(i_object1._com, i_object2._com))

    def add_new_inverse(self, element: Reference, inverse: int) -> HybridShapeInverse:
        return HybridShapeInverse(self.hybrid_shape_factory.AddNewInverse(element._com, inverse))

    def add_new_join(self, element1: Reference, element2: Reference) -> HybridShapeAssemble:
        return HybridShapeAssemble(self.hybrid_shape_factory.AddNewJoin(element1._com, element2._com))

    def add_new_law_dist_proj(self, i_reference: Reference, i_definition: Reference) -> HybridShapeLawDistProj:
        return HybridShapeLawDistProj(self.hybrid_shape_factory.AddNewLawDistProj(i_reference._com, i_definition._com))

    def add_new_line_angle(self, i_curve: Reference, i_surface: Reference, i_point: Reference, i_geodesic: bool, i_begin_offset: float, i_end_offset: float, i_angle: float, i_orientation: bool) -> HybridShapeLineAngle:
        return HybridShapeLineAngle(self.hybrid_shape_factory.AddNewLineAngle(i_curve._com, i_surface._com, i_point._com, i_geodesic, i_begin_offset, i_end_offset, i_angle, i_orientation))

    def add_new_line_bi_tangent(self, i_curve1: Reference, i_element2: Reference, i_support: Reference) -> HybridShapeLineBiTangent:
        return HybridShapeLineBiTangent(self.hybrid_shape_factory.AddNewLineBiTangent(i_curve1._com, i_element2._com, i_support._com))

    def add_new_line_bisecting(self, i_line1: Reference, i_line2: Reference, i_begin_offset: float, i_end_offset: float, i_orientation: bool, solution_nb: int) -> HybridShapeLineBisecting:
        return HybridShapeLineBisecting(self.hybrid_shape_factory.AddNewLineBisecting(i_line1._com, i_line2._com, i_begin_offset, i_end_offset, i_orientation, solution_nb))

    def add_new_line_bisecting_on_support(self, i_line1: Reference, i_line2: Reference, i_surface: Reference, i_begin_offset: float, i_end_offset: float, i_orientation: bool, solution_nb: int) -> HybridShapeLineBisecting:
        return HybridShapeLineBisecting(self.hybrid_shape_factory.AddNewLineBisectingOnSupport(i_line1._com, i_line2._com, i_surface._com, i_begin_offset, i_end_offset, i_orientation, solution_nb))

    def add_new_line_bisecting_on_support_with_point(self, i_line1: Reference, i_line2: Reference, i_ref_point: Reference, i_surface: Reference, i_begin_offset: float, i_end_offset: float, i_orientation: bool, solution_nb: int) -> HybridShapeLineBisecting:
        return HybridShapeLineBisecting(self.hybrid_shape_factory.AddNewLineBisectingOnSupportWithPoint(i_line1._com, i_line2._com, i_ref_point._com, i_surface._com, i_begin_offset, i_end_offset, i_orientation, solution_nb))

    def add_new_line_bisecting_with_point(self, i_line1: Reference, i_line2: Reference, i_ref_point: Reference, i_begin_offset: float, i_end_offset: float, i_orientation: bool, solution_nb: int) -> HybridShapeLineBisecting:
        return HybridShapeLineBisecting(self.hybrid_shape_factory.AddNewLineBisectingWithPoint(i_line1._com, i_line2._com, i_ref_point._com, i_begin_offset, i_end_offset, i_orientation, solution_nb))

    def add_new_line_datum(self, i_object: Reference) -> HybridShapeLineExplicit:
        return HybridShapeLineExplicit(self.hybrid_shape_factory.AddNewLineDatum(i_object._com))

    def add_new_line_normal( self, i_surface: Reference, i_point: Reference, i_begin_offset: float,  i_end_offset: float, i_orientation: bool) -> HybridShapeLineNormal:
        return HybridShapeLineNormal(self.hybrid_shape_factory.AddNewLineNormal(i_surface._com, i_point._com, i_begin_offset, i_end_offset, i_orientation) )

    def add_new_line_pt_dir(self, i_pt: Reference, i_direction: HybridShapeDirection, i_begin_offset: float, i_end_offset: float, i_orientation: bool) -> HybridShapeLinePtDir:
        return HybridShapeLinePtDir(self.hybrid_shape_factory.AddNewLinePtDir(i_pt._com, i_direction._com, i_begin_offset, i_end_offset, i_orientation))

    def add_new_line_pt_dir_on_support(self, i_pt: Reference, i_direction: HybridShapeDirection, i_support: Reference, i_begin_offset: float, i_end_offset: float, i_orientation: bool) -> HybridShapeLinePtDir:
        return HybridShapeLinePtDir(self.hybrid_shape_factory.AddNewLinePtDirOnSupport(i_pt._com, i_direction._com, i_support._com, i_begin_offset, i_end_offset, i_orientation))

    def add_new_line_pt_pt(self, i_pt_origine: Reference or AnyObject, i_pt_extremite: Reference or AnyObject) -> HybridShapeLinePtPt:
        return HybridShapeLinePtPt(self.hybrid_shape_factory.AddNewLinePtPt(i_pt_origine._com, i_pt_extremite._com))

    def add_new_line_pt_pt_extended(self, i_pt_origine: Reference, i_pt_extremite: Reference, i_begin_offset: float, i_end_offset: float) -> HybridShapeLinePtPt:
        return HybridShapeLinePtPt(self.hybrid_shape_factory.AddNewLinePtPtExtended(i_pt_origine._com, i_pt_extremite._com, i_begin_offset, i_end_offset))

    def add_new_line_pt_pt_on_support(self, i_pt_origine: Reference, i_pt_extremite: Reference, i_support: Reference) -> HybridShapeLinePtPt:
        return HybridShapeLinePtPt(self.hybrid_shape_factory.AddNewLinePtPtOnSupport(i_pt_origine._com, i_pt_extremite._com, i_support._com))

    def add_new_line_pt_pt_on_support_extended(self, i_pt_origine: Reference, i_pt_extremite: Reference, i_support: Reference, i_begin_offset: float, i_end_offset: float) -> HybridShapeLinePtPt:
        return HybridShapeLinePtPt(self.hybrid_shape_factory.AddNewLinePtPtOnSupportExtended(i_pt_origine._com, i_pt_extremite._com, i_support._com, i_begin_offset, i_end_offset))

    def add_new_line_tangency(self, i_curve: Reference, i_point: Reference, i_begin_offset: float, i_end_offset: float, i_orientation: bool) -> HybridShapeLineTangency:
        return HybridShapeLineTangency(self.hybrid_shape_factory.AddNewLineTangency(i_curve._com, i_point._com, i_begin_offset, i_end_offset, i_orientation))

    def add_new_line_tangency_on_support(self, i_curve: Reference, i_point: Reference, i_support: Reference, i_begin_offset: float, i_end_offset: float, i_orientation: bool) -> HybridShapeLineTangency:
        return HybridShapeLineTangency(self.hybrid_shape_factory.AddNewLineTangencyOnSupport(i_curve._com, i_point._com, i_support._com, i_begin_offset, i_end_offset, i_orientation))

    def add_new_loft(self) -> HybridShapeLoft:
        return HybridShapeLoft(self.hybrid_shape_factory.AddNewLoft())

    def add_new_mid_surface(self, i_support: Reference, i_creation_mode: int, i_threshold: float) -> HybridShapeMidSurface:
        return HybridShapeMidSurface(self.hybrid_shape_factory.AddNewMidSurface(i_support._com, i_creation_mode, i_threshold))

    def add_new_mid_surface_with_auto_threshold(self, i_support: Reference, i_creation_mode: int, i_threshold: float, i_auto_thickness_threshold: int) -> HybridShapeMidSurface:
        return HybridShapeMidSurface(self.hybrid_shape_factory.AddNewMidSurfaceWithAutoThreshold(i_support._com, i_creation_mode, i_threshold, i_auto_thickness_threshold))

    def add_new_near(self, multi_element: Reference, reference_element: Reference) -> HybridShapeNear:
        return HybridShapeNear(self.hybrid_shape_factory.AddNewNear( multi_element._com, reference_element._com))

    def add_new_offset(self, i_object_to_offset: Reference, i_offset: float, i_orientation: bool, i_precision: float) -> HybridShapeOffset:
        return HybridShapeOffset(self.hybrid_shape_factory.AddNewOffset(i_object_to_offset._com, i_offset, i_orientation, i_precision))

    def add_new_plane1_curve(self, i_planar_curve: Reference) -> HybridShapePlane1Curve:
        return HybridShapePlane1Curve(self.hybrid_shape_factory.AddNewPlane1Curve(i_planar_curve._com))

    def add_new_plane1_line1_pt(self, i_ln: Reference, i_pt: Reference) -> HybridShapePlane1Line1Pt:
        return HybridShapePlane1Line1Pt(self.hybrid_shape_factory.AddNewPlane1Line1Pt(i_ln._com, i_pt._com))

    def add_new_plane2_lines(self, i_ln1: Reference, i_ln2: Reference) -> HybridShapePlane2Lines:
        return HybridShapePlane2Lines(self.hybrid_shape_factory.AddNewPlane2Lines(i_ln1._com, i_ln2._com))

    def add_new_plane3_points(self, i_pt1: Reference, i_pt2: Reference, i_pt3: Reference) -> HybridShapePlane3Points:
        return HybridShapePlane3Points(self.hybrid_shape_factory.AddNewPlane3Points(i_pt1._com, i_pt2._com, i_pt3._com))

    def add_new_plane_angle(self, i_plane: Reference, i_revol_axis: Reference, i_angle: float, i_orientation: bool) -> HybridShapePlaneAngle:
        return HybridShapePlaneAngle( self.hybrid_shape_factory.AddNewPlaneAngle( i_plane._com, i_revol_axis._com, i_angle, i_orientation ))

    def add_new_plane_between(self, i_plane1: Reference, i_plane2: Reference, i_ratio: float, i_orientation: int) -> HybridShapePlaneBetween:
        return HybridShapePlaneBetween(i_plane1, i_plane2, i_ratio, i_orientation)

    def add_new_plane_datum(self, i_object: Reference) -> HybridShapePlaneExplicit:
        return HybridShapePlaneExplicit(self.hybrid_shape_factory.AddNewPlaneDatum(i_object.com))

    def add_new_plane_equation(self, i_a_coeff: float, i_b_coeff: float, i_c_coeff: float, i_d_coeff: float) -> HybridShapePlaneEquation:
        return HybridShapePlaneEquation(self.hybrid_shape_factory.AddNewPlaneEquation(i_a_coeff, i_b_coeff, i_c_coeff, i_d_coeff))

    def add_new_plane_mean(self, i_list_of_points: tuple, nb_point: int) -> HybridShapePlaneMean:
        return HybridShapePlaneMean(self.hybrid_shape_factory.AddNewPlaneMean(i_list_of_points, nb_point))

    def add_new_plane_normal(self, i_curve: Reference, i_pt: Reference) -> HybridShapePlaneNormal:
        return HybridShapePlaneNormal(self.hybrid_shape_factory.AddNewPlaneNormal(i_curve.com, i_pt.com))

    def add_new_plane_offset(self, i_plane: Reference, i_offset: float, i_orientation: bool) -> HybridShapePlaneOffset:
        return HybridShapePlaneOffset(self.hybrid_shape_factory.AddNewPlaneOffset(i_plane._com, i_offset, i_orientation))

    def add_new_plane_offset_pt(self, i_plane: Reference, i_pt: Reference) -> HybridShapePlaneOffsetPt:
        return HybridShapePlaneOffsetPt(self.hybrid_shape_factory.AddNewPlaneOffsetPt(i_plane._com, i_pt._com))

    def add_new_plane_tangent(self, i_surface: Reference, i_pt: Reference) -> HybridShapePlaneTangent:
        return HybridShapePlaneTangent(self.hybrid_shape_factory.AddNewPlaneTangent(i_surface._com, i_pt._com))

    def add_new_point_between(self, i_point1: Reference, i_point2: Reference, i_ratio: float, i_orientation: int) -> HybridShapePointBetween:
        return HybridShapePointBetween(self.hybrid_shape_factory.AddNewPointBetween(i_point1._com,i_point2._com,i_ratio,i_orientation))

    def add_new_point_center(self, i_curve: Reference) -> HybridShapePointCenter:
        return HybridShapePointCenter(self.hybrid_shape_factory.AddNewPointCenter(i_curve.com))

    def add_new_point_coord(self, i_x: float, i_y: float, i_z: float) -> HybridShapePointCoord:
        return HybridShapePointCoord(self.hybrid_shape_factory.AddNewPointCoord(i_x, i_y, i_z))

    def add_new_point_coords(self, coord_list):
        """
        coord_list must be a list of iterables of length 3.
        Example: coord_list = [[0, 0, 1], [0, 1, 0]]
        :param list() coord_list:
        :returns: list[HybridShapePointCoord]
        """

        r = []
        for coord in coord_list:
            r.append(self.add_new_point_coord(coord[0], coord[1], coord[2]))
        return r

    def add_new_point_coord_with_reference(self, i_x: float, i_y: float, i_z: float, i_pt: Reference) -> HybridShapePointCoord:
        return HybridShapePointCoord(self.hybrid_shape_factory.AddNewPointCoordWithReference(i_x, i_y, i_z, i_pt._com))

    def add_new_point_datum(self, i_object: Reference) -> HybridShapePointExplicit:
        return HybridShapePointExplicit(self.hybrid_shape_factory.AddNewPointDatum(i_object.com))

    def add_new_point_on_curve_along_direction(self, i_crv: Reference, i_long: float, i_orientation: bool, i_direction: HybridShapeDirection) -> HybridShapePointOnCurve:
        return HybridShapePointOnCurve(self.hybrid_shape_factory.AddNewPointOnCurveAlongDirection(i_crv._com, i_long, i_orientation, i_direction._com))

    def add_new_point_on_curve_from_distance(self, i_crv: Reference, i_long: float, i_orientation: bool) -> HybridShapePointOnCurve:
        return HybridShapePointOnCurve(self.hybrid_shape_factory.AddNewPointOnCurveFromDistance(i_crv._com, i_long, i_orientation))

    def add_new_point_on_curve_from_percent(self, i_crv: Reference, i_long: float, i_orientation: bool) -> HybridShapePointOnCurve:
        return HybridShapePointOnCurve(self.hybrid_shape_factory.AddNewPointOnCurveFromPercent(i_crv._com, i_long, i_orientation))

    def add_new_point_on_curve_with_reference_along_direction(self, i_crv: Reference, i_pt: Reference, i_long: float, i_orientation: bool, i_direction: HybridShapeDirection) -> HybridShapePointOnCurve:
        return HybridShapePointOnCurve(self.hybrid_shape_factory.AddNewPointOnCurveWithReferenceAlongDirection(i_crv._com, i_pt._com, i_long, i_orientation, i_direction._com))

    def add_new_point_on_curve_with_reference_from_distance(self, i_crv: Reference, i_pt: Reference, i_long: float, i_orientation: bool) -> HybridShapePointOnCurve:
        return HybridShapePointOnCurve(self.hybrid_shape_factory.AddNewPointOnCurveWithReferenceFromDistance(i_crv._com, i_pt._com, i_long, i_orientation))

    def add_new_point_on_curve_with_reference_from_percent(self, i_crv: Reference, i_pt: Reference, i_long: float, i_orientation: bool) -> HybridShapePointOnCurve:
        return HybridShapePointOnCurve(self.hybrid_shape_factory.AddNewPointOnCurveWithReferenceFromPercent(i_crv._com, i_pt._com, i_long, i_orientation))

    def add_new_point_on_plane(self, i_plane: Reference, i_x: float, i_y: float) -> HybridShapePointOnPlane:
        return HybridShapePointOnPlane(self.hybrid_shape_factory.AddNewPointOnPlane(i_plane.com, i_x, i_y))

    def add_new_point_on_plane_with_reference(self, i_plane: Reference, i_pt: Reference, i_x: float, i_y: float) -> HybridShapePointOnPlane:
        return HybridShapePointOnPlane(self.hybrid_shape_factory.AddNewPointOnPlaneWithReference(i_plane._com, i_pt._com, i_x, i_y))

    def add_new_point_on_surface(self, i_surface: Reference, i_direction: HybridShapeDirection, i_x: float) -> HybridShapePointOnSurface:
        return HybridShapePointOnSurface(self.hybrid_shape_factory.AddNewPointOnSurface(i_surface._com, i_direction._com, i_x))

    def add_new_point_on_surface_with_reference(self, i_surface: Reference, i_pt: Reference, i_direction: HybridShapeDirection, i_x: float) -> HybridShapePointOnSurface:
        return HybridShapePointOnSurface(self.hybrid_shape_factory.AddNewPointOnSurfaceWithReference(i_surface._com, i_pt._com, i_direction._com, i_x))

    def add_new_point_tangent(self, i_curve: Reference, i_direction: HybridShapeDirection) -> HybridShapePointTangent:
        return HybridShapePointTangent(self.hybrid_shape_factory.AddNewPointTangent(i_curve._com, i_direction._com))

    def add_new_polyline(self) -> HybridShapePolyline:
        return HybridShapePolyline(self.hybrid_shape_factory.AddNewPolyline())

    def add_new_position_transfo(self, i_mode: int) -> HybridShapePositionTransfo:
        return HybridShapePositionTransfo(self.hybrid_shape_factory.AddNewPositionTransfo(i_mode))

    def add_new_project(self, i_element: Reference, i_support: Reference) -> HybridShapeProject:
        return HybridShapeProject(self.hybrid_shape_factory.AddNewProject(i_element._com, i_support._com))

    def add_new_reflect_line(self, i_support: Reference, i_dir: HybridShapeDirection, i_angle: float, i_orientation_support: int, i_orientation_direction: int) -> HybridShapeReflectLine:
        return HybridShapeReflectLine(self.hybrid_shape_factory.AddNewReflectLine(i_support._com, i_dir._com, i_angle,i_orientation_support,i_orientation_direction))

    def add_new_reflect_line_with_type(self, i_support: Reference, i_dir: HybridShapeDirection, i_angle: float, i_orientation_support: int, i_orientation_direction: int, i_type: int) -> HybridShapeReflectLine:
        return HybridShapeReflectLine(self.hybrid_shape_factory.AddNewReflectLineWithType(i_support._com, i_dir._com, i_angle, i_orientation_support, i_orientation_direction, i_type))

    def add_new_revol(self, i_object_to_extrude: Reference, i_offset_debut: float, i_offset_fin: float, i_axis: Reference) -> HybridShapeRevol:
        return HybridShapeRevol(self.hybrid_shape_factory.AddNewRevol(i_object_to_extrude._com, i_offset_debut, i_offset_fin, i_axis._com))

    def add_new_rotate(self, i_to_rotate: Reference, i_axis: Reference, i_angle: float) -> HybridShapeRotate:
        return HybridShapeRotate(self.hybrid_shape_factory.AddNewRotate(i_to_rotate._com, i_axis._com, i_angle))

    def add_new_section(self) -> HybridShapeSection:
        return HybridShapeSection(self.hybrid_shape_factory.AddNewSection())

    def add_new_sphere(self, i_center: Reference, i_axis: Reference, i_radius: float, i_begin_parallel_angle: float, i_end_parallel_angle: float, i_begin_meridian_angle: float, i_end_meridian_angle: float) -> HybridShapeSphere:
        return HybridShapeSphere(self.hybrid_shape_factory.AddNewSphere(i_center._com, i_axis._com, i_radius, i_begin_parallel_angle, i_end_parallel_angle, i_begin_meridian_angle, i_end_meridian_angle))

    def add_new_spine(self) -> HybridShapeSpine:
        return HybridShapeSpine(self.hybrid_shape_factory.AddNewSpine())

    def add_new_spiral(self, i_type: int, i_support: Reference, i_center_point: Reference, i_axis: HybridShapeDirection, i_starting_radius: float, i_clockwise_revolution: bool) -> HybridShapeSpiral:
        return HybridShapeSpiral(self.hybrid_shape_factory.AddNewSpiral(i_type, i_support._com, i_center_point._com, i_axis._com, i_starting_radius, i_clockwise_revolution))

    def add_new_spline(self) -> HybridShapeSpline:
        return HybridShapeSpline(self.hybrid_shape_factory.AddNewSpline())

    def add_new_surface_datum(self, i_object: Reference) -> HybridShapeSurfaceExplicit:
        return HybridShapeSurfaceExplicit(self.hybrid_shape_factory.AddNewSurfaceDatum(i_object._com))

    def add_new_sweep_circle(self, i_guide1: Reference) -> HybridShapeSweepCircle:
        return HybridShapeSweepCircle(self.hybrid_shape_factory.AddNewSweepCircle(i_guide1._com))

    def add_new_sweep_conic(self, ip_ia_guide1: Reference) -> HybridShapeSweepConic:
        return HybridShapeSweepConic(self.hybrid_shape_factory.AddNewSweepConic(ip_ia_guide1._com))

    def add_new_sweep_explicit(self, i_profile: Reference, i_guide: Reference) -> HybridShapeSweepExplicit:
        return HybridShapeSweepExplicit(self.hybrid_shape_factory.AddNewSweepExplicit(i_profile._com, i_guide._com ))

    def add_new_sweep_line(self, i_guide1: Reference) -> HybridShapeSweepLine:
        return HybridShapeSweepLine(self.hybrid_shape_factory.AddNewSweepLine(i_guide1._com))

    def add_new_symmetry(self, i_object: Reference, i_reference: Reference) -> HybridShapeSymmetry:
        return HybridShapeSymmetry(self.hybrid_shape_factory.AddNewSymmetry(i_object._com, i_reference._com))

    def add_new_transfer(self, i_element_to_transfer: Reference, i_type_of_transfer: int) -> HybridShapeTransfer:
        return HybridShapeTransfer(self.hybrid_shape_factory.AddNewTransfer(i_element_to_transfer._com, i_type_of_transfer))

    def add_new_translate(self, i_element: Reference, i_direction: HybridShapeDirection, i_distance: float) -> HybridShapeTranslate:
        return HybridShapeTranslate(self.hybrid_shape_factory.AddNewTranslate(i_element._com, i_direction._com, i_distance))

    def add_new_unfold(self) -> HybridShapeUnfold:
        return HybridShapeUnfold(self.hybrid_shape_factory.AddNewUnfold())

    def add_new_volume_datum(self, i_object: Reference) -> HybridShapeVolumeExplicit:
        return HybridShapeVolumeExplicit(self.hybrid_shape_factory.AddNewVolumeDatum(i_object._com))

    def add_new_wrap_curve(self) -> HybridShapeWrapCurve:
        return HybridShapeWrapCurve(self.hybrid_shape_factory.AddNewWrapCurve())

    def add_new_wrap_surface(self, i_body_to_deform: Reference) -> HybridShapeWrapSurface:
        return HybridShapeWrapSurface(self.hybrid_shape_factory.AddNewWrapSurface(i_body_to_deform._com))

    def change_feature_name(self, i_elem: Reference, name: str) -> None:
        return self.hybrid_shape_factory.ChangeFeatureName(i_elem._com, name)

    def delete_object_for_datum(self, i_object: Reference) -> None:
        return self.hybrid_shape_factory.DeleteObjectForDatum(i_object._com)

    def gsm_visibility(self, i_elem: Reference, show: int) -> None:
        return self.hybrid_shape_factory.GSMVisibility(i_elem.com, show)

    def get_geometrical_feature_type(self, i_elem: Reference) -> int:
        """
        :return: 0 = Unknown, 1 = Point, 2 = Curve, 3 = Line, 4 = Circle, 5 = Surface, 6 = Plane, 7 = Solid, Volume
        """
        return self.hybrid_shape_factory.GetGeometricalFeatureType(i_elem._com)

    def __repr__(self):
        return f'HybridShapeFactory(name="{self.name}")'