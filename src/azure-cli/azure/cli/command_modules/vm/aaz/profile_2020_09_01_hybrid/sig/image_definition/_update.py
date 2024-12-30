# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "sig image-definition update",
)
class Update(AAZCommand):
    """Update a VM Image definition.

    :example: Change the shared image definition's recommended configuration
        az sig image-definition update --resource-group MyResourceGroup --gallery-name MyGallery --gallery-image-definition MyImage --resource-group MyResourceGroup --set recommended.vCpUs.min=myNewvCpUsMin recommended.vCpUs.max=myNewvCpUsMax recommended.memory.min=myNewMemoryMin recommended.memory.max=myNewMemoryMax description="newDescription"

    :example: Remove a shared image definition's configuration property
        az sig image-definition update --resource-group MyResourceGroup --gallery-name MyGallery --gallery-image-definition MyImage --resource-group MyResourceGroup --remove recommended.vCpUs.min
    """

    _aaz_info = {
        "version": "2021-10-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.compute/galleries/{}/images/{}", "2021-10-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.gallery_image_definition = AAZStrArg(
            options=["-i", "--gallery-image-definition"],
            help="The name of the gallery image definition to be retrieved.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.gallery_name = AAZStrArg(
            options=["-r", "--gallery-name"],
            help="The name of the Shared Image Gallery in which the Image Definition resides.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "GalleryImage"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="GalleryImage",
            help="Resource location",
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="GalleryImage",
            help="Resource tags",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.architecture = AAZStrArg(
            options=["--architecture"],
            arg_group="Properties",
            help="The architecture of the image. Applicable to OS disks only.",
            nullable=True,
            enum={"Arm64": "Arm64", "x64": "x64"},
        )
        _args_schema.description = AAZStrArg(
            options=["--description"],
            arg_group="Properties",
            help="The description of this gallery image definition resource. This property is updatable.",
            nullable=True,
        )
        _args_schema.disallowed = AAZObjectArg(
            options=["--disallowed"],
            arg_group="Properties",
            help="Describes the disallowed disk types.",
            nullable=True,
        )
        _args_schema.end_of_life_date = AAZDateTimeArg(
            options=["--end-of-life-date"],
            arg_group="Properties",
            help="The end of life date of the gallery image definition. This property can be used for decommissioning purposes. This property is updatable.",
            nullable=True,
        )
        _args_schema.eula = AAZStrArg(
            options=["--eula"],
            arg_group="Properties",
            help="The Eula agreement for the gallery image definition.",
            nullable=True,
        )
        _args_schema.features = AAZListArg(
            options=["--features"],
            arg_group="Properties",
            help="A list of gallery image features.",
            nullable=True,
        )
        _args_schema.hyper_v_generation = AAZStrArg(
            options=["--hyper-v-generation"],
            arg_group="Properties",
            help="The hypervisor generation of the Virtual Machine. Applicable to OS disks only.",
            nullable=True,
            enum={"V1": "V1", "V2": "V2"},
        )
        _args_schema.identifier = AAZObjectArg(
            options=["--identifier"],
            arg_group="Properties",
            help="This is the gallery image definition identifier.",
        )
        _args_schema.os_state = AAZStrArg(
            options=["--os-state"],
            arg_group="Properties",
            help="This property allows the user to specify whether the virtual machines created under this image are 'Generalized' or 'Specialized'.",
            enum={"Generalized": "Generalized", "Specialized": "Specialized"},
        )
        _args_schema.os_type = AAZStrArg(
            options=["--os-type"],
            arg_group="Properties",
            help="This property allows you to specify the type of the OS that is included in the disk when creating a VM from a managed image. <br><br> Possible values are: <br><br> **Windows** <br><br> **Linux**",
            enum={"Linux": "Linux", "Windows": "Windows"},
        )
        _args_schema.privacy_statement_uri = AAZStrArg(
            options=["--privacy-statement-uri"],
            arg_group="Properties",
            help="The privacy statement uri.",
            nullable=True,
        )
        _args_schema.purchase_plan = AAZObjectArg(
            options=["--purchase-plan"],
            arg_group="Properties",
            help="Describes the gallery image definition purchase plan. This is used by marketplace images.",
            nullable=True,
        )
        _args_schema.recommended = AAZObjectArg(
            options=["--recommended"],
            arg_group="Properties",
            help="The properties describe the recommended machine configuration for this Image Definition. These properties are updatable.",
            nullable=True,
        )
        _args_schema.release_note_uri = AAZStrArg(
            options=["--release-note-uri"],
            arg_group="Properties",
            help="The release note uri.",
            nullable=True,
        )

        disallowed = cls._args_schema.disallowed
        disallowed.disk_types = AAZListArg(
            options=["disk-types"],
            help="A list of disk types.",
            nullable=True,
        )

        disk_types = cls._args_schema.disallowed.disk_types
        disk_types.Element = AAZStrArg(
            nullable=True,
        )

        features = cls._args_schema.features
        features.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.features.Element
        _element.name = AAZStrArg(
            options=["name"],
            help="The name of the gallery image feature.",
            nullable=True,
        )
        _element.value = AAZStrArg(
            options=["value"],
            help="The value of the gallery image feature.",
            nullable=True,
        )

        identifier = cls._args_schema.identifier
        identifier.offer = AAZStrArg(
            options=["offer"],
            help="The name of the gallery image definition offer.",
        )
        identifier.publisher = AAZStrArg(
            options=["publisher"],
            help="The name of the gallery image definition publisher.",
        )
        identifier.sku = AAZStrArg(
            options=["sku"],
            help="The name of the gallery image definition SKU.",
        )

        purchase_plan = cls._args_schema.purchase_plan
        purchase_plan.name = AAZStrArg(
            options=["name"],
            help="The plan ID.",
            nullable=True,
        )
        purchase_plan.product = AAZStrArg(
            options=["product"],
            help="The product ID.",
            nullable=True,
        )
        purchase_plan.publisher = AAZStrArg(
            options=["publisher"],
            help="The publisher ID.",
            nullable=True,
        )

        recommended = cls._args_schema.recommended
        recommended.memory = AAZObjectArg(
            options=["memory"],
            nullable=True,
        )
        cls._build_args_resource_range_update(recommended.memory)
        recommended.v_cp_us = AAZObjectArg(
            options=["v-cp-us"],
            help="Describes the resource range.",
            nullable=True,
        )
        cls._build_args_resource_range_update(recommended.v_cp_us)
        return cls._args_schema

    _args_resource_range_update = None

    @classmethod
    def _build_args_resource_range_update(cls, _schema):
        if cls._args_resource_range_update is not None:
            _schema.max = cls._args_resource_range_update.max
            _schema.min = cls._args_resource_range_update.min
            return

        cls._args_resource_range_update = AAZObjectArg(
            nullable=True,
        )

        resource_range_update = cls._args_resource_range_update
        resource_range_update.max = AAZIntArg(
            options=["max"],
            help="The maximum number of the resource.",
            nullable=True,
        )
        resource_range_update.min = AAZIntArg(
            options=["min"],
            help="The minimum number of the resource.",
            nullable=True,
        )

        _schema.max = cls._args_resource_range_update.max
        _schema.min = cls._args_resource_range_update.min

    def _execute_operations(self):
        self.pre_operations()
        self.GalleryImagesGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.GalleryImagesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class GalleryImagesGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "galleryImageName", self.ctx.args.gallery_image_definition,
                    required=True,
                ),
                **self.serialize_url_param(
                    "galleryName", self.ctx.args.gallery_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2021-10-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_gallery_image_read(cls._schema_on_200)

            return cls._schema_on_200

    class GalleryImagesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "galleryImageName", self.ctx.args.gallery_image_definition,
                    required=True,
                ),
                **self.serialize_url_param(
                    "galleryName", self.ctx.args.gallery_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2021-10-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_gallery_image_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("architecture", AAZStrType, ".architecture")
                properties.set_prop("description", AAZStrType, ".description")
                properties.set_prop("disallowed", AAZObjectType, ".disallowed")
                properties.set_prop("endOfLifeDate", AAZStrType, ".end_of_life_date")
                properties.set_prop("eula", AAZStrType, ".eula")
                properties.set_prop("features", AAZListType, ".features")
                properties.set_prop("hyperVGeneration", AAZStrType, ".hyper_v_generation")
                properties.set_prop("identifier", AAZObjectType, ".identifier", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("osState", AAZStrType, ".os_state", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("osType", AAZStrType, ".os_type", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("privacyStatementUri", AAZStrType, ".privacy_statement_uri")
                properties.set_prop("purchasePlan", AAZObjectType, ".purchase_plan")
                properties.set_prop("recommended", AAZObjectType, ".recommended")
                properties.set_prop("releaseNoteUri", AAZStrType, ".release_note_uri")

            disallowed = _builder.get(".properties.disallowed")
            if disallowed is not None:
                disallowed.set_prop("diskTypes", AAZListType, ".disk_types")

            disk_types = _builder.get(".properties.disallowed.diskTypes")
            if disk_types is not None:
                disk_types.set_elements(AAZStrType, ".")

            features = _builder.get(".properties.features")
            if features is not None:
                features.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.features[]")
            if _elements is not None:
                _elements.set_prop("name", AAZStrType, ".name")
                _elements.set_prop("value", AAZStrType, ".value")

            identifier = _builder.get(".properties.identifier")
            if identifier is not None:
                identifier.set_prop("offer", AAZStrType, ".offer", typ_kwargs={"flags": {"required": True}})
                identifier.set_prop("publisher", AAZStrType, ".publisher", typ_kwargs={"flags": {"required": True}})
                identifier.set_prop("sku", AAZStrType, ".sku", typ_kwargs={"flags": {"required": True}})

            purchase_plan = _builder.get(".properties.purchasePlan")
            if purchase_plan is not None:
                purchase_plan.set_prop("name", AAZStrType, ".name")
                purchase_plan.set_prop("product", AAZStrType, ".product")
                purchase_plan.set_prop("publisher", AAZStrType, ".publisher")

            recommended = _builder.get(".properties.recommended")
            if recommended is not None:
                _UpdateHelper._build_schema_resource_range_update(recommended.set_prop("memory", AAZObjectType, ".memory"))
                _UpdateHelper._build_schema_resource_range_update(recommended.set_prop("vCPUs", AAZObjectType, ".v_cp_us"))

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    @classmethod
    def _build_schema_resource_range_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("max", AAZIntType, ".max")
        _builder.set_prop("min", AAZIntType, ".min")

    _schema_gallery_image_read = None

    @classmethod
    def _build_schema_gallery_image_read(cls, _schema):
        if cls._schema_gallery_image_read is not None:
            _schema.id = cls._schema_gallery_image_read.id
            _schema.location = cls._schema_gallery_image_read.location
            _schema.name = cls._schema_gallery_image_read.name
            _schema.properties = cls._schema_gallery_image_read.properties
            _schema.tags = cls._schema_gallery_image_read.tags
            _schema.type = cls._schema_gallery_image_read.type
            return

        cls._schema_gallery_image_read = _schema_gallery_image_read = AAZObjectType()

        gallery_image_read = _schema_gallery_image_read
        gallery_image_read.id = AAZStrType(
            flags={"read_only": True},
        )
        gallery_image_read.location = AAZStrType(
            flags={"required": True},
        )
        gallery_image_read.name = AAZStrType(
            flags={"read_only": True},
        )
        gallery_image_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        gallery_image_read.tags = AAZDictType()
        gallery_image_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_gallery_image_read.properties
        properties.architecture = AAZStrType()
        properties.description = AAZStrType()
        properties.disallowed = AAZObjectType()
        properties.end_of_life_date = AAZStrType(
            serialized_name="endOfLifeDate",
        )
        properties.eula = AAZStrType()
        properties.features = AAZListType()
        properties.hyper_v_generation = AAZStrType(
            serialized_name="hyperVGeneration",
        )
        properties.identifier = AAZObjectType(
            flags={"required": True},
        )
        properties.os_state = AAZStrType(
            serialized_name="osState",
            flags={"required": True},
        )
        properties.os_type = AAZStrType(
            serialized_name="osType",
            flags={"required": True},
        )
        properties.privacy_statement_uri = AAZStrType(
            serialized_name="privacyStatementUri",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.purchase_plan = AAZObjectType(
            serialized_name="purchasePlan",
        )
        properties.recommended = AAZObjectType()
        properties.release_note_uri = AAZStrType(
            serialized_name="releaseNoteUri",
        )

        disallowed = _schema_gallery_image_read.properties.disallowed
        disallowed.disk_types = AAZListType(
            serialized_name="diskTypes",
        )

        disk_types = _schema_gallery_image_read.properties.disallowed.disk_types
        disk_types.Element = AAZStrType()

        features = _schema_gallery_image_read.properties.features
        features.Element = AAZObjectType()

        _element = _schema_gallery_image_read.properties.features.Element
        _element.name = AAZStrType()
        _element.value = AAZStrType()

        identifier = _schema_gallery_image_read.properties.identifier
        identifier.offer = AAZStrType(
            flags={"required": True},
        )
        identifier.publisher = AAZStrType(
            flags={"required": True},
        )
        identifier.sku = AAZStrType(
            flags={"required": True},
        )

        purchase_plan = _schema_gallery_image_read.properties.purchase_plan
        purchase_plan.name = AAZStrType()
        purchase_plan.product = AAZStrType()
        purchase_plan.publisher = AAZStrType()

        recommended = _schema_gallery_image_read.properties.recommended
        recommended.memory = AAZObjectType()
        cls._build_schema_resource_range_read(recommended.memory)
        recommended.v_cp_us = AAZObjectType(
            serialized_name="vCPUs",
        )
        cls._build_schema_resource_range_read(recommended.v_cp_us)

        tags = _schema_gallery_image_read.tags
        tags.Element = AAZStrType()

        _schema.id = cls._schema_gallery_image_read.id
        _schema.location = cls._schema_gallery_image_read.location
        _schema.name = cls._schema_gallery_image_read.name
        _schema.properties = cls._schema_gallery_image_read.properties
        _schema.tags = cls._schema_gallery_image_read.tags
        _schema.type = cls._schema_gallery_image_read.type

    _schema_resource_range_read = None

    @classmethod
    def _build_schema_resource_range_read(cls, _schema):
        if cls._schema_resource_range_read is not None:
            _schema.max = cls._schema_resource_range_read.max
            _schema.min = cls._schema_resource_range_read.min
            return

        cls._schema_resource_range_read = _schema_resource_range_read = AAZObjectType()

        resource_range_read = _schema_resource_range_read
        resource_range_read.max = AAZIntType()
        resource_range_read.min = AAZIntType()

        _schema.max = cls._schema_resource_range_read.max
        _schema.min = cls._schema_resource_range_read.min


__all__ = ["Update"]