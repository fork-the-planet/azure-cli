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
    "sig image-version wait",
)
class Wait(AAZWaitCommand):
    """Place the CLI in a waiting state until a condition is met.
    """

    _aaz_info = {
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.compute/galleries/{}/images/{}/versions/{}", "2023-07-03"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

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
            help="The name of the gallery image definition in which the Image Version resides.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.gallery_image_version_name = AAZStrArg(
            options=["-e", "--gallery-image-version", "--gallery-image-version-name"],
            help="The name of the gallery image version to be deleted.",
            required=True,
            id_part="child_name_2",
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
        _args_schema.expand = AAZStrArg(
            options=["--expand"],
            help="The expand expression to apply on the operation.",
            enum={"ReplicationStatus": "ReplicationStatus", "UefiSettings": "UefiSettings"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.GalleryImageVersionsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=False)
        return result

    class GalleryImageVersionsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName}/versions/{galleryImageVersionName}",
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
                    "galleryImageVersionName", self.ctx.args.gallery_image_version_name,
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
                    "$expand", self.ctx.args.expand,
                ),
                **self.serialize_query_param(
                    "api-version", "2023-07-03",
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

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.publishing_profile = AAZObjectType(
                serialized_name="publishingProfile",
            )
            properties.replication_status = AAZObjectType(
                serialized_name="replicationStatus",
                flags={"read_only": True},
            )
            properties.safety_profile = AAZObjectType(
                serialized_name="safetyProfile",
            )
            properties.security_profile = AAZObjectType(
                serialized_name="securityProfile",
            )
            properties.storage_profile = AAZObjectType(
                serialized_name="storageProfile",
                flags={"required": True},
            )

            publishing_profile = cls._schema_on_200.properties.publishing_profile
            publishing_profile.end_of_life_date = AAZStrType(
                serialized_name="endOfLifeDate",
            )
            publishing_profile.exclude_from_latest = AAZBoolType(
                serialized_name="excludeFromLatest",
            )
            publishing_profile.published_date = AAZStrType(
                serialized_name="publishedDate",
                flags={"read_only": True},
            )
            publishing_profile.replica_count = AAZIntType(
                serialized_name="replicaCount",
            )
            publishing_profile.replication_mode = AAZStrType(
                serialized_name="replicationMode",
            )
            publishing_profile.storage_account_type = AAZStrType(
                serialized_name="storageAccountType",
            )
            publishing_profile.target_extended_locations = AAZListType(
                serialized_name="targetExtendedLocations",
            )
            publishing_profile.target_regions = AAZListType(
                serialized_name="targetRegions",
            )

            target_extended_locations = cls._schema_on_200.properties.publishing_profile.target_extended_locations
            target_extended_locations.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.publishing_profile.target_extended_locations.Element
            _element.encryption = AAZObjectType()
            _WaitHelper._build_schema_encryption_images_read(_element.encryption)
            _element.extended_location = AAZObjectType(
                serialized_name="extendedLocation",
            )
            _element.extended_location_replica_count = AAZIntType(
                serialized_name="extendedLocationReplicaCount",
            )
            _element.name = AAZStrType()
            _element.storage_account_type = AAZStrType(
                serialized_name="storageAccountType",
            )

            extended_location = cls._schema_on_200.properties.publishing_profile.target_extended_locations.Element.extended_location
            extended_location.name = AAZStrType()
            extended_location.type = AAZStrType()

            target_regions = cls._schema_on_200.properties.publishing_profile.target_regions
            target_regions.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.publishing_profile.target_regions.Element
            _element.encryption = AAZObjectType()
            _WaitHelper._build_schema_encryption_images_read(_element.encryption)
            _element.exclude_from_latest = AAZBoolType(
                serialized_name="excludeFromLatest",
            )
            _element.name = AAZStrType(
                flags={"required": True},
            )
            _element.regional_replica_count = AAZIntType(
                serialized_name="regionalReplicaCount",
            )
            _element.storage_account_type = AAZStrType(
                serialized_name="storageAccountType",
            )

            replication_status = cls._schema_on_200.properties.replication_status
            replication_status.aggregated_state = AAZStrType(
                serialized_name="aggregatedState",
                flags={"read_only": True},
            )
            replication_status.summary = AAZListType(
                flags={"read_only": True},
            )

            summary = cls._schema_on_200.properties.replication_status.summary
            summary.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.replication_status.summary.Element
            _element.details = AAZStrType(
                flags={"read_only": True},
            )
            _element.progress = AAZIntType(
                flags={"read_only": True},
            )
            _element.region = AAZStrType(
                flags={"read_only": True},
            )
            _element.state = AAZStrType(
                flags={"read_only": True},
            )

            safety_profile = cls._schema_on_200.properties.safety_profile
            safety_profile.allow_deletion_of_replicated_locations = AAZBoolType(
                serialized_name="allowDeletionOfReplicatedLocations",
            )
            safety_profile.policy_violations = AAZListType(
                serialized_name="policyViolations",
                flags={"read_only": True},
            )
            safety_profile.reported_for_policy_violation = AAZBoolType(
                serialized_name="reportedForPolicyViolation",
                flags={"read_only": True},
            )

            policy_violations = cls._schema_on_200.properties.safety_profile.policy_violations
            policy_violations.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.safety_profile.policy_violations.Element
            _element.category = AAZStrType()
            _element.details = AAZStrType()

            security_profile = cls._schema_on_200.properties.security_profile
            security_profile.uefi_settings = AAZObjectType(
                serialized_name="uefiSettings",
            )

            uefi_settings = cls._schema_on_200.properties.security_profile.uefi_settings
            uefi_settings.additional_signatures = AAZObjectType(
                serialized_name="additionalSignatures",
            )
            uefi_settings.signature_template_names = AAZListType(
                serialized_name="signatureTemplateNames",
            )

            additional_signatures = cls._schema_on_200.properties.security_profile.uefi_settings.additional_signatures
            additional_signatures.db = AAZListType()
            additional_signatures.dbx = AAZListType()
            additional_signatures.kek = AAZListType()
            additional_signatures.pk = AAZObjectType()
            _WaitHelper._build_schema_uefi_key_read(additional_signatures.pk)

            db = cls._schema_on_200.properties.security_profile.uefi_settings.additional_signatures.db
            db.Element = AAZObjectType()
            _WaitHelper._build_schema_uefi_key_read(db.Element)

            dbx = cls._schema_on_200.properties.security_profile.uefi_settings.additional_signatures.dbx
            dbx.Element = AAZObjectType()
            _WaitHelper._build_schema_uefi_key_read(dbx.Element)

            kek = cls._schema_on_200.properties.security_profile.uefi_settings.additional_signatures.kek
            kek.Element = AAZObjectType()
            _WaitHelper._build_schema_uefi_key_read(kek.Element)

            signature_template_names = cls._schema_on_200.properties.security_profile.uefi_settings.signature_template_names
            signature_template_names.Element = AAZStrType()

            storage_profile = cls._schema_on_200.properties.storage_profile
            storage_profile.data_disk_images = AAZListType(
                serialized_name="dataDiskImages",
            )
            storage_profile.os_disk_image = AAZObjectType(
                serialized_name="osDiskImage",
            )
            storage_profile.source = AAZObjectType()

            data_disk_images = cls._schema_on_200.properties.storage_profile.data_disk_images
            data_disk_images.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.storage_profile.data_disk_images.Element
            _element.host_caching = AAZStrType(
                serialized_name="hostCaching",
            )
            _element.lun = AAZIntType(
                flags={"required": True},
            )
            _element.size_in_gb = AAZIntType(
                serialized_name="sizeInGB",
                flags={"read_only": True},
            )
            _element.source = AAZObjectType()
            _WaitHelper._build_schema_gallery_disk_image_source_read(_element.source)

            os_disk_image = cls._schema_on_200.properties.storage_profile.os_disk_image
            os_disk_image.host_caching = AAZStrType(
                serialized_name="hostCaching",
            )
            os_disk_image.size_in_gb = AAZIntType(
                serialized_name="sizeInGB",
                flags={"read_only": True},
            )
            os_disk_image.source = AAZObjectType()
            _WaitHelper._build_schema_gallery_disk_image_source_read(os_disk_image.source)

            source = cls._schema_on_200.properties.storage_profile.source
            source.community_gallery_image_id = AAZStrType(
                serialized_name="communityGalleryImageId",
            )
            source.id = AAZStrType()
            source.virtual_machine_id = AAZStrType(
                serialized_name="virtualMachineId",
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _WaitHelper:
    """Helper class for Wait"""

    _schema_encryption_images_read = None

    @classmethod
    def _build_schema_encryption_images_read(cls, _schema):
        if cls._schema_encryption_images_read is not None:
            _schema.data_disk_images = cls._schema_encryption_images_read.data_disk_images
            _schema.os_disk_image = cls._schema_encryption_images_read.os_disk_image
            return

        cls._schema_encryption_images_read = _schema_encryption_images_read = AAZObjectType()

        encryption_images_read = _schema_encryption_images_read
        encryption_images_read.data_disk_images = AAZListType(
            serialized_name="dataDiskImages",
        )
        encryption_images_read.os_disk_image = AAZObjectType(
            serialized_name="osDiskImage",
        )

        data_disk_images = _schema_encryption_images_read.data_disk_images
        data_disk_images.Element = AAZObjectType()

        _element = _schema_encryption_images_read.data_disk_images.Element
        _element.disk_encryption_set_id = AAZStrType(
            serialized_name="diskEncryptionSetId",
        )
        _element.lun = AAZIntType(
            flags={"required": True},
        )

        os_disk_image = _schema_encryption_images_read.os_disk_image
        os_disk_image.disk_encryption_set_id = AAZStrType(
            serialized_name="diskEncryptionSetId",
        )
        os_disk_image.security_profile = AAZObjectType(
            serialized_name="securityProfile",
        )

        security_profile = _schema_encryption_images_read.os_disk_image.security_profile
        security_profile.confidential_vm_encryption_type = AAZStrType(
            serialized_name="confidentialVMEncryptionType",
        )
        security_profile.secure_vm_disk_encryption_set_id = AAZStrType(
            serialized_name="secureVMDiskEncryptionSetId",
        )

        _schema.data_disk_images = cls._schema_encryption_images_read.data_disk_images
        _schema.os_disk_image = cls._schema_encryption_images_read.os_disk_image

    _schema_gallery_disk_image_source_read = None

    @classmethod
    def _build_schema_gallery_disk_image_source_read(cls, _schema):
        if cls._schema_gallery_disk_image_source_read is not None:
            _schema.id = cls._schema_gallery_disk_image_source_read.id
            _schema.storage_account_id = cls._schema_gallery_disk_image_source_read.storage_account_id
            _schema.uri = cls._schema_gallery_disk_image_source_read.uri
            return

        cls._schema_gallery_disk_image_source_read = _schema_gallery_disk_image_source_read = AAZObjectType()

        gallery_disk_image_source_read = _schema_gallery_disk_image_source_read
        gallery_disk_image_source_read.id = AAZStrType()
        gallery_disk_image_source_read.storage_account_id = AAZStrType(
            serialized_name="storageAccountId",
        )
        gallery_disk_image_source_read.uri = AAZStrType()

        _schema.id = cls._schema_gallery_disk_image_source_read.id
        _schema.storage_account_id = cls._schema_gallery_disk_image_source_read.storage_account_id
        _schema.uri = cls._schema_gallery_disk_image_source_read.uri

    _schema_uefi_key_read = None

    @classmethod
    def _build_schema_uefi_key_read(cls, _schema):
        if cls._schema_uefi_key_read is not None:
            _schema.type = cls._schema_uefi_key_read.type
            _schema.value = cls._schema_uefi_key_read.value
            return

        cls._schema_uefi_key_read = _schema_uefi_key_read = AAZObjectType()

        uefi_key_read = _schema_uefi_key_read
        uefi_key_read.type = AAZStrType()
        uefi_key_read.value = AAZListType()

        value = _schema_uefi_key_read.value
        value.Element = AAZStrType()

        _schema.type = cls._schema_uefi_key_read.type
        _schema.value = cls._schema_uefi_key_read.value


__all__ = ["Wait"]