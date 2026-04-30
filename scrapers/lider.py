import requests
import json
import time

class LiderScraper:
    def __init__(self, cat_id='66849718_44699651', sort='price_high'):
        self.cat_id = cat_id
        self.sort = sort
        self.cookies = {
            'vtc': 'Uer6NrHb61tEPXaluEHK48',
            'bstc': 'Uer6NrHb61tEPXaluEHK48',
            'xpa': '9p9zr|_2gcb|ov7Vm',
            'exp-ck': 'ov7Vm1',
            'ACID': '3f9ca933-72f7-4f46-9095-f60d6e93e0d7',
            'locDataV3': 'eyJmdWxmaWxsbWVudE9wdGlvbiI6IlNISVBQSU5HIiwicGlja3VwU3RvcmUiOnsiYWNjZXNzUG9pbnRJZCI6Ijc2IiwiYWNjZXNzVHlwZSI6IlBJQ0tVUF9JTlNUT1JFIiwiYWRkcmVzc0xpbmVPbmUiOiJFbGlnZSB0dSBtw6l0b2RvIGRlIGVudHJlZ2EiLCJjaXR5IjoiU2FudGlhZ28iLCJjb3VudHJ5Q29kZSI6IkNMIiwiZnVsZmlsbG1lbnRPcHRpb24iOiJQSUNLVVAiLCJmdWxmaWxsbWVudFR5cGUiOiJJTlNUT1JFX1BJQ0tVUF9JTlNUT1JFIiwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOi0zMy40MjQ4NDc2LCJsb25naXR1ZGUiOi03MC41NTk4NTAzNjE2MjEyfSwicG9zdGFsQ29kZSI6IiIsImRpc3BsYXlOYW1lIjoibGFzIGNvbmRlcyIsInN0YXRlT3JQcm92aW5jZUNvZGUiOiJSZWdpw7NuIE1ldHJvcG9saXRhbmEiLCJzdG9yZklkIjoiMDAwMDAwMDMwNiIsInN0b3JlSHJzIjp7InN0YXJ0IjoiMDowMGFtIiwiZW5kIjoiMTE6NTlwbSJ9fSwic2hpcHBpbmciOnsicG9zdGFsQ29kZSI6IiIsImNpdHkiOiJTYW50aWFnbyIsInN0YXRlT3JQcm92aW5jZUNvZGUiOiJSZWdpw7NuIE1ldHJvcG9saXRhbmEiLCJjb3VudHJ5Q29kZSI6IkNMIiwibGF0aXR1ZGUiOi0zMy40MjQ4NDc2LCJsb25naXR1ZGUiOi03MC41NTk4NTAzNjE2MjEyLCJpc1BvQm94IjpmYWxzZSwiaXNBcG9GcG8iOmZhbHNlfSwiaXNEZWZhdWx0U3RvcmUiOnRydWUsImlzRXhwbGljaXRJbnRlbnQiOmZhbHNlLCJhc3NvcnRtZW50Ijp7ImludGVudCI6IlNISVBQSU5HIiwic3RvcmVJZCI6IjAwMDAwMDAzMDYifSwicmVmcmVzaEF0IjoxNzc3NTcxMzAzMTU0LCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6M2Y5Y2E5MzMtNzJmNy00ZjQ2LTkwOTUtZjYwZDZlOTNlMGQ3In0=',
            'hasLocData': '1',
            'userAppVersion': 'main-1.189.0-e268c13-0427T1001',
            '_astc': '1b498f20bd8422a5e747a6114e4b7936',
            '_pxvid': '6784431c-44b4-11f1-8ba9-b722baa50115',
            'pxcts': '678453b7-44b4-11f1-8ba9-a30e9869de63',
            '__pxvid': '67adfb83-44b4-11f1-ba1d-be7237728d07',
            'cartId': '67aae0d0-44b4-11f1-a1bf-5d4efd5591d6',
            'adblocked': 'true',
            '_px3': '7a3acae92c06da8fe11eb5bb895301e270acc9ba6c3ba913f0a27fa032706849:X7tV8YicKzQ2N+PW6rweZaK49uZHy77k/WaIqLF/F9jfQ0KLJUxtClNdUA4XPFxsHLPuJEvm0qrVq0efeIDTfQ==:1000:qG3FFt1bHJl6CMqVS2pQIAkwWGh9p34u3NSNiiwYRnJjzw+/yUuHbcp4lPF7Zw+3z3Yg7q2QDdR4eXnTwCsdHcxVQOuDCyHZBvq99P2DX772ZMCi6/BWoeeGpjnOARVR07MTTnwhkhDcaZCoJpMFYP+Yk1p2IG1h2L5WC+VhLwjiVwKo377zERtPkMCr7Td9Yk11K7OTushfxDWU1wBm+O4PuJvPMxGpBth7ZIhXgGVtVT3BFUzhaEuT7eM9h6SIiQysA14l0eAWYHwg0NA5P6C4kW9waU9qh2AFXHE7mPgghT1+dfNqVx/v5Vl4UaIj1ZpajVB1XHYd7RNDARf9xvHlXSfV8TwE/nMyRUGVNO0YBJC6d5qjSlTtL2npEwQDgy5kO84XCaViW09mY3DZd3q3/hdcOPlGKq8LDmr8z1pVgpblnyIWyeKF6XZETnm9X6OCPuBZ1XdRICr2Eh4yS6DEpJzoQ+prGuKcHzu3jX4fMLqmUfFzEODR8i3lVOAQ',
            'xpth': 'x-o-vertical%2BEA',
            'xpm': '1%2B1777567714%2BUer6NrHb61tEPXaluEHK48~%2B1',
            'TS01cc7ea9': '01ee6f2633a9266cf841fc50a8542bdd57d3e88102be70c3797b3694106daaa589c211f3cdb5e64d1f802de374e880d289c68e8975',
            'TS017e8d10': '01ee6f2633a9266cf841fc50a8542bdd57d3e88102be70c3797b3694106daaa589c211f3cdb5e64d1f802de374e880d289c68e8975',
            'TS01fffdff': '01ee6f2633a9266cf841fc50a8542bdd57d3e88102be70c3797b3694106daaa589c211f3cdb5e64d1f802de374e880d289c68e8975',
            'TSe3289311027': '08d516a33fab2000f34fbb357c034416e15fefbdfaa5b166d90799bbd838e285d908ad080982ba07087c5f32191130007c71ce5858cac684ce96b0d53a0097d19cfb4d2317ffc30b38e7759faa3b94deee3245d7af7e5d62c55bfc1c03312ea1',
        }
        import random
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0'
        ]
        selected_ua = random.choice(user_agents)

        self.headers = {
            'accept': 'application/json',
            'accept-language': 'es-CL',
            'baggage': 'trafficType=customer,deviceType=desktop,renderScope=CSR,webRequestSource=Browser,pageName=browseResults,isomorphicSessionId=znrU7qXZDs0imLy4nwYwD,renderViewId=44878002-ee67-46dd-9090-74a8cd2b7311,requestTs=1777567904297,tpid=00-18ab30974bb4265ba6d529cd0e9168f0-8972202c3eaca2d8-00',
            'content-type': 'application/json',
            'origin': 'https://www.lider.cl',
            'priority': 'u=1, i',
            'referer': f'https://www.lider.cl/browse/tecno/tv/{self.cat_id}?sort={self.sort}',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'traceparent': '00-18ab30974bb4265ba6d529cd0e9168f0-8972202c3eaca2d8-00',
            'user-agent': selected_ua,
            'wm_mp': 'true',
            'wm_page_url': f'https://www.lider.cl/browse/tecno/tv/{self.cat_id}?sort={self.sort}',
            'wm_qos.correlation_id': '6_5f0eNO9xZuZMa19IdehCYFvOhjQqgCqilm',
            'x-apollo-operation-name': 'Browse',
            'x-enable-server-timing': '1',
            'x-latency-trace': '1',
            'x-o-bu': 'LIDER-CL',
            'x-o-ccm': 'server',
            'x-o-correlation-id': '6_5f0eNO9xZuZMa19IdehCYFvOhjQqgCqilm',
            'x-o-gql-query': 'query Browse',
            'x-o-mart': 'B2C',
            'x-o-platform': 'rweb',
            'x-o-platform-version': 'main-1.189.0-e268c13-0427T1001',
            'x-o-segment': 'oaoh',
            'x-o-vertical': 'EA',
        }
        # Nota: json_data se construye con los valores iniciales.
        # El loop de scrape actualizará la página.
        self.json_data = {
            'query': 'query Browse( $query:String $limit:Int $page:Int $prg:Prg! $facet:String $sort:Sort $catId:String! $max_price:String $min_price:String $module_search:String $affinityOverride:AffinityOverride $pap:String $ps:Int $ptss:String $beShelfId:String $fitmentFieldParams:JSON ={}$fitmentSearchParams:JSON ={}$searchParams:JSON ={}$rawFacet:String $seoPath:String $trsp:String $fetchMarquee:Boolean! $fetchSkyline:Boolean! $fetchGallery:Boolean! $fetchSbaTop:Boolean! $fetchDataV1:Boolean! $fetchDataV2:Boolean = false $fungibilityEnabled:Boolean! $enableAdsPromoData:Boolean = false $fetchDac:Boolean! $additionalQueryParams:JSON ={}$enablePortableFacets:Boolean = false $enableFashionTopNav:Boolean = false $intentSource:IntentSource $tenant:String! $enableFacetCount:Boolean = true $pageType:String! = "BrowsePage" $marketSpecificParams:String $enableMultiSave:Boolean = false $enableVariantCount:Boolean = false $fSeo:Boolean = true $enableSellerType:Boolean = false $enableItemRank:Boolean = false $enableOptimisticWeightUpdate:Boolean = false $enableAdditionalSearchDepartmentAnalytics:Boolean = false $enableFulfillmentTagsEnhacements:Boolean = false $disableAds:Boolean = false $enableRxDrugScheduleModal:Boolean = false $enablePromoData:Boolean = false $fetchBadSplit:Boolean = false $enableSeoLangUrl:Boolean = false $enableSignInToSeePrice:Boolean = false $enableImageBannerCarousel:Boolean = false $enableHero4:Boolean = false $enableInStoreShelfMessage:Boolean = false $enableShopSimilarBottomSheet:Boolean = false $enablePromotionMessages:Boolean = false $enableDebugAnalyticsTags:Boolean = false $enableItemLimits:Boolean = false $enableCanAddToList:Boolean = false $enableIsFreeWarranty:Boolean = false $enableSimpleEmailSignUp:Boolean = false $enableDesktopHighlights:Boolean = false $enableVolumePricing:Boolean = false $enableGenericSeo:Boolean = false $enableCopyBlock:Boolean = false $enableSeoBrowseMetaDataShortDesc:Boolean = false $enableSlaBadgeV2:Boolean = false $enableUnifiedSchema:Boolean = false $enableNavigationTokensBrowse:Boolean = false $enableUnifiedProductFragment:Boolean = false $enableESSCarousel:Boolean = false $version:String = "v1" $enableAdsTemplateBadging:Boolean = false ){search( query:$query limit:$limit page:$page prg:$prg pap:$pap facet:$facet sort:$sort cat_id:$catId max_price:$max_price min_price:$min_price module_search:$module_search affinityOverride:$affinityOverride additionalQueryParams:$additionalQueryParams ps:$ps ptss:$ptss trsp:$trsp intentSource:$intentSource _be_shelf_id:$beShelfId pageType:$pageType enableSlaBadgeV2:$enableSlaBadgeV2 ){query searchResult{...BrowseResultFragment}}contentLayout( channel:"WWW" pageType:$pageType tenant:$tenant version:$version p13n:{page:$page userReqInfo:{refererContext:{catId:$catId}enableSlaBadgeV2:$enableSlaBadgeV2}}searchArgs:{query:$query cat_id:$catId _be_shelf_id:$beShelfId prg:$prg}){modules( p13n:{page:$page userReqInfo:{refererContext:{catId:$catId}enableSlaBadgeV2:$enableSlaBadgeV2}}){...ModuleFragment configs{__typename...on EnricherModuleConfigsV1{zoneV1}...on TempoWM_GLASSWWWEmailSignUpWidgetConfigs{_rawConfigs}...GenericSortAndFilterModule...on TempoWM_GLASSWWWPillsModuleConfigs @skip(if:$enableNavigationTokensBrowse){moduleSource enablePillsModuleReposition pillsV2{...GenericPillsModuleFragment}}...TileTakeOverProductFragment @skip(if:$enableUnifiedSchema)...TileTakeOverProductUnifiedFragment @include(if:$enableUnifiedSchema)...PrismTileTakeOverFragment...TileDisplayAdFragment...on TempoWM_GLASSWWWSearchFitmentModuleConfigs{fitments( fitmentSearchParams:$fitmentSearchParams fitmentFieldParams:$fitmentFieldParams ){...FitmentFragment sisFitmentResponse{...BrowseResultFragment}}}...on TempoWM_GLASSWWWSearchACCStoreSelectionConfigs{ctaText userInfoMessage headingDetails{heading headingWhenFulfillmentIsSelectedAsPickup}}...on TempoWM_GLASSWWWStoreSelectionHeaderConfigs{fulfillmentMethodLabel storeDislayName}...on TempoWM_GLASSWWWSponsoredProductCarouselConfigs{_rawConfigs}...on _TempoWM_GLASSWWWSearchHeaderModuleConfigs{_rawConfigs}...on NavigationTokensModuleConfigs @include(if:$enableNavigationTokensBrowse){_rawConfigs}...on TempoWM_GLASSWWWBenefitProgramBannerPlaceholderConfigs{_rawConfigs}...on TempoWM_GLASSWWWBrowseRelatedShelves @include(if:$fSeo){seoBrowseRelmData( id:$catId marketSpecificParams:$marketSpecificParams ){relm{id url name}}}...TopNavFragment @include(if:$enableFashionTopNav)...EnhancedCategoryNavFragment...BrandAmplifierAdConfigs @include(if:$fetchSbaTop)...PopularInBrowseFragment...CopyBlockModuleFragment @include(if:$enableCopyBlock)...BannerModuleFragment...Hero4FragmentV2 @include(if:$enableHero4)...HeroPOVFragment...InlineSearchModuleFragment...MarqueeDisplayAdConfigsFragment @include(if:$fetchMarquee)...SkylineDisplayAdConfigsFragment @include(if:$fetchSkyline)...GalleryDisplayAdConfigsFragment @include(if:$fetchGallery)...DynamicAdContainerConfigsFragment @include(if:$fetchDac)...HorizontalChipModuleConfigsFragment...SkinnyBannerFragment @skip(if:$enableUnifiedSchema)...SkinnyBannerConfigsUnifiedFragment @include(if:$enableUnifiedSchema)...GenericSeoFaqFragment @include(if:$enableGenericSeo)...SponsoredVideoAdFragment @skip(if:$fungibilityEnabled)...AdPlaceholderModuleConfigsFragment @include(if:$fungibilityEnabled)...AlertBannerListFragment...ImageBannerCarouselFragment @include(if:$enableImageBannerCarousel)...SimpleEmailSignUpFragment @include(if:$enableSimpleEmailSignUp)...MosaicGridFragment...FaqFragment}}...LayoutFragment pageMetadata{location{pickupStore deliveryStore intent postalCode stateOrProvinceCode city storeId accessPointId accessType spokeNodeId storeFrontIds intentStrength}pageContext}}seoBrowseMetaData( id:$catId facets:$rawFacet path:$seoPath facet_query_param:$facet _be_shelf_id:$beShelfId marketSpecificParams:$marketSpecificParams page:$page ){metaTitle metaDesc metaCanon h1 shortDesc @include(if:$enableSeoBrowseMetaDataShortDesc) noIndex languageUrls{name url}breadCrumb{cat_level id name url}}}fragment BrowseResultFragment on SearchInterface{title aggregatedCount...GenericBreadCrumbFragment...ShelfDataFragment...GenericDebugFragment...GenericItemStacksFragment...GenericPageMetaDataFragment...GenericPaginationFragment...GenericRequestContextFragment...GenericErrorResponse modules{facetsV1 @skip(if:$enablePortableFacets){...GenericFacetFragment}topNavFacets @include(if:$enablePortableFacets){...GenericFacetFragment}allSortAndFilterFacets @include(if:$enablePortableFacets){...GenericFacetFragment}pills{...GenericPillsModuleFragment}bannerMessages{message type linkText linkUrl}}pac{relevantPT{productType score}showPAC reasonCode}navigationTokens{type navigationBeacon{displayType}tokens{displayName url imageUrl tokenBeacon}}}fragment ModuleFragment on TempoModule{__typename type name version moduleId schedule{priority}matchedTrigger{zone}}fragment LayoutFragment on ContentLayout{layouts{id layout}}fragment GenericBreadCrumbFragment on SearchInterface{breadCrumb{id name url cat_level}}fragment ShelfDataFragment on SearchInterface{shelfData{shelfName shelfId}}fragment GenericDebugFragment on SearchInterface{debug{statusCode responseTimeMillis scsTimeMillis sisUrl adsUrl genAIDebugInfo{searchAlgorithm isGenAiQueryEligible genAIUnavailableReason reformulatedQuery}presoDebugInformation{explainerToolsResponse analyticsTags @include(if:$enableDebugAnalyticsTags)}}}fragment GenericItemStacksFragment on SearchInterface{itemStacks{displayMessage meta{beacon suppressTitle isSponsored adsBeacon{adUuid moduleInfo max_ads adSlots}spBeaconInfo{adUuid moduleInfo pageViewUUID placement max}query isPartialResult stackId stackType stackName title description subTitle titleKey subType queryUsedForSearchResults layoutEnum totalItemCount totalItemCountDisplay viewAllParams{query cat_id sort facet affinityOverride recall_set groupIdentifier min_price max_price view_module shouldHide buttonTitle}comparisonCart{product_type}borderColor iconUrl initialCount fulfillmentIntent}itemsV2{...GenericItemFragment @skip(if:$enableUnifiedProductFragment)...UnifiedProductFragment @include(if:$enableUnifiedProductFragment)...GenericInGridMarqueeAdFragment @skip(if:$disableAds)...GenericInGridAdFragment @skip(if:$disableAds)...GenericTileTakeOverTileFragment...GenericTileTakeOverPrismFragment...InlineCategoryNavigationFragment...EssCarouselFragment @include(if:$enableESSCarousel)}content{title subtitle data{type name displayName url urlParams imageUrl}}}}fragment UnifiedProductFragment on Product{__typename buyBoxSuppression similarItems id usItemId specialCtaType @include(if:$enableSignInToSeePrice) isBadSplit @include(if:$fetchBadSplit) catalogSellerId rxDrugScheduleType @include(if:$enableRxDrugScheduleModal) wfsEnabled @include(if:$enableSellerType) itemRank @include(if:$enableItemRank) fitmentLabel name checkStoreAvailabilityATC seeShippingEligibility productBrand type shortDescription averageWeight weightIncrement topResult additionalOfferCount availabilityInNearbyStore itemBeacon catalogProductType collectibles{gradingCompany collectibleGrade}gradingTypeCode conditionPriceRange{otherConditionsMessage minPriceDisplay}imageInfo{...UnifiedProductImageInfoFragment}aspectInfo{name header id snippet}plItem{isPLItemToBoost plItemTagString}canonicalUrl conditionV2{code groupCode}externalInfo{url}itemType productAttributes @include(if:$enableDesktopHighlights){productHighlights{name value}}promotionMessages @include(if:$enablePromotionMessages){type badgeBackgroundColor badgeStyleId badgeTextColor badgeTitle bundledDisplayName expiryDateMessage limitMessage message popupMessage specialMessage}category{categoryPathId path{name url}}returnPolicy{returnable freeReturns returnWindow{value unitType}returnPolicyText}discounts{...UnifiedProductDiscountsFragment}badges{flags{__typename...on BaseBadge{key bundleId @include(if:$enableMultiSave) text type id styleId}...on PreviouslyPurchasedBadge{id text key lastBoughtOn numBought}}tags{__typename...on BaseBadge{key text type}}groups{__typename name members{...on BadgeGroupMember{__typename id key memberType otherInfo{moqText}rank textTemplate textValues slaText slaDate slaDateISO sla{regular faster unscheduled}styleId text type iconId templates{regular faster unavailable}badgeContent{type value styleId id canonicalUrl athAsset athModule}}...on CompositeGroupMember{__typename join memberType styleId suffix members{__typename id key memberType rank textTemplate textValues slaText styleId text type iconId}}}}...UnifiedBadgeFragment}buyNowEligible classType averageRating numberOfReviews esrb mediaRating salesUnitType sellerId sellerName sellerType hasSellerBadge isEarlyAccessItem preEarlyAccessEvent earlyAccessEvent blitzItem annualEvent annualEventV2 availabilityStatusV2{display value}availabilityMessage @include(if:$enableInStoreShelfMessage) groupMetaData{groupType groupSubType numberOfComponents groupComponents{quantity offerId componentType productDisplayName}}addOnServices{...UnifiedAddOnServicesFragment}productLocation{displayValue aisle{zone aisle}}fulfillmentSpeed offerId offerType @include(if:$enableFulfillmentTagsEnhacements) preOrder{...UnifiedPreorderFragment}pac{showPAC reasonCode fulfillmentPacModule pacType pacTypeV2 remainingPAC}droneAttributes{droneAccessType}fulfillmentSummary{fulfillment storeId deliveryDate fulfillmentMethods fulfillmentBadge outOfCountryEligible}priceInfo{...UnifiedProductPriceInfoFragment}variantCount @include(if:$enableVariantCount) variantCriteria{...UnifiedVariantCriteriaFragment}snapEligible fulfillmentTitle fulfillmentType manufacturerName showAtc showSubscribe socialInfo{socialHandleName}p13nDataV1{predictedQuantity}p13nDataV2{predictedQuantity}sponsoredProduct{spQs clickBeacon spTags viewBeacon}showOptions showBuyNow quickShop quickShopCTALabel rewards{eligible state minQuantity rewardAmt promotionId selectionToken rewardMultiplierStr cbOffer term expiry description}promoData @include(if:$enablePromoData){type terms templateData{priceString imageUrl}}promoDiscount{discount discountEligible discountEligibleVariantPresent promotionId promoOffer state showOtherEligibleItemsCTA type min awardValue awardSubType maxPerTxn maxPerOrder tiers{awardValue minQuantity}}arExperiences{isARHome isZeekit isAROptical}eventAttributes{...UnifiedProductEventAttributesFragment}subscription{subscriptionEligible subscriptionTransactable showSubscriptionCTA}hasCarePlans petRx{eligible singleDispense}vision{ageGroup visionCenterApproved}showExploreOtherConditionsCTA isPreowned pglsCondition newConditionProductId preownedCondition keyAttributes{displayEnum value}mhmdFlag seeSimilar isSimilarLookEligible @include(if:$enableShopSimilarBottomSheet) winningProductId @include(if:$enableShopSimilarBottomSheet) orderLimit @include(if:$enableItemLimits) orderMinLimit @include(if:$enableItemLimits) canAddToList @include(if:$enableCanAddToList) isFreeWarranty @include(if:$enableIsFreeWarranty) isQSRItem isCustomizable}fragment UnifiedProductPriceInfoFragment on ProductPriceInfo{priceRange{minPrice maxPrice priceString}subscriptionDiscountPrice{priceString}currentPrice{...UnifiedProductPriceFragment priceDisplay}comparisonPrice{...UnifiedProductPriceFragment}wasPrice{...UnifiedProductPriceFragment}unitPrice{...UnifiedProductPriceFragment}listPrice{...UnifiedProductPriceFragment}savingsAmount{...UnifiedProductSavingsFragment}shipPrice{...UnifiedProductPriceFragment}additionalFees{dutyFee{price}}subscriptionPrice{priceString subscriptionString downPaymentString}priceDisplayCodes{priceDisplayCondition finalCostByWeight submapType isB2BPrice priceDisplayType}wPlusEarlyAccessPrice{memberPrice{...UnifiedProductPriceFragment}savings{...UnifiedProductSavingsFragment}eventStartTime eventStartTimeDisplay}subscriptionDualPrice subscriptionPercentage volumePriceTiers @include(if:$enableVolumePricing){currencyUnit minUnit price savingsAmount}taxInfo{isTaxable}priceDetails{...UnifiedProductPriceDetailsFragment}}fragment UnifiedProductSavingsFragment on ProductSavings{amount percent priceString}fragment UnifiedProductPriceFragment on ProductPrice{price priceString variantPriceString priceType currencyUnit priceDisplay supportText}fragment UnifiedProductPriceDetailsFragment on ProductPriceDetails{currency priceLines{lineType values{key value}}}fragment UnifiedProductEventAttributesFragment on EventAttributes{priceFlip specialBuy}fragment UnifiedPreorderFragment on PreOrder{isPreOrder preOrderMessage preOrderStreetDateMessage streetDate streetDateDisplayable streetDateType releaseDate}fragment UnifiedVariantCriteriaFragment on VariantCriterion{name type id displayName isVariantTypeSwatch isVariantTypeAllowed variantList{id images name rank displayName swatchImageUrl availabilityStatus products selectedProduct{canonicalUrl usItemId}}}fragment UnifiedProductDiscountsFragment on Discounts{discountedValue{price priceString}discountMetaData{id type savings{amount priceString percent}price{price priceString priceDisplay}unitPrice{price priceString}comparisonPrice{price priceString}unitPriceDisplayCondition}}fragment UnifiedProductImageInfoFragment on ProductImageInfo{id name thumbnailUrl size allImages{id url type}}fragment UnifiedBadgeFragment on UnifiedBadge{labels{key text}groupsV2{name pos flow members{memType memId memStyleId content{type value styleId contDesc url actionId actionContent{type contentId value styleId}}}}}fragment UnifiedAddOnServicesFragment on AddOnService{serviceType serviceTitle serviceSubTitle serviceProviders groups{groupType groupTitle assetUrl shortDescription unavailabilityReason nearByStores{nodes{id displayName distance}}services{offerId}}}fragment GenericItemFragment on Product{__typename buyBoxSuppression similarItems id usItemId specialCtaType @include(if:$enableSignInToSeePrice) isBadSplit @include(if:$fetchBadSplit) catalogSellerId rxDrugScheduleType @include(if:$enableRxDrugScheduleModal) wfsEnabled @include(if:$enableSellerType) itemRank @include(if:$enableItemRank) averageWeight @include(if:$enableOptimisticWeightUpdate) fitmentLabel name checkStoreAvailabilityATC seeShippingEligibility brand type shortDescription averageWeight weightIncrement topResult additionalOfferCount availabilityInNearbyStore itemBeacon catalogProductType collectibles{gradingCompany collectibleGrade}gradingTypeCode conditionPriceRange{otherConditionsMessage minPriceDisplay}imageInfo{...GenericProductImageInfoFragment}aspectInfo{name header id snippet}plItem{isPLItemToBoost plItemTagString}canonicalUrl conditionV2{code groupCode}externalInfo{url}itemType productAttributes @include(if:$enableDesktopHighlights){productHighlights{name value}}promotionMessages @include(if:$enablePromotionMessages){type badgeBackgroundColor badgeStyleId badgeTextColor badgeTitle bundledDisplayName expiryDateMessage limitMessage message popupMessage specialMessage}category{categoryPathId path{name url}}returnPolicy{returnable freeReturns returnWindow{value unitType}returnPolicyText}discounts{...GenericProductDiscountsFragment}conditionV2{code groupCode}badges{flags{__typename...on BaseBadge{key bundleId @include(if:$enableMultiSave) text type id styleId}...on PreviouslyPurchasedBadge{id text key lastBoughtOn numBought}}tags{__typename...on BaseBadge{key text type}}groups{__typename name members{...on BadgeGroupMember{__typename id key memberType otherInfo{moqText}rank textTemplate textValues slaText slaDate slaDateISO sla{regular faster unscheduled}styleId text type iconId templates{regular faster unavailable}badgeContent{type value styleId id canonicalUrl athAsset athModule}}...on CompositeGroupMember{__typename join memberType styleId suffix members{__typename id key memberType rank textTemplate textValues slaText styleId text type iconId}}}}...GenericBadgeFragment}buyNowEligible classType averageRating numberOfReviews esrb mediaRating salesUnitType sellerId sellerName sellerType hasSellerBadge isEarlyAccessItem preEarlyAccessEvent earlyAccessEvent blitzItem annualEvent annualEventV2 availabilityStatusV2{display value}availabilityMessage @include(if:$enableInStoreShelfMessage) groupMetaData{groupType groupSubType numberOfComponents groupComponents{quantity offerId componentType productDisplayName}}addOnServices{...AddOnServicesFragment}productLocation{displayValue aisle{zone aisle}}fulfillmentSpeed offerId offerType @include(if:$enableFulfillmentTagsEnhacements) preOrder{...GenericPreorderFragment}pac{showPAC reasonCode fulfillmentPacModule}droneAttributes{droneAccessType}fulfillmentSummary{fulfillment storeId deliveryDate fulfillmentMethods fulfillmentBadge outOfCountryEligible}priceInfo{...GenericProductPriceInfoFragment}variantCount @include(if:$enableVariantCount) variantCriteria{...GenericVariantCriteriaFragment}snapEligible fulfillmentTitle fulfillmentType brand manufacturerName showAtc sponsoredProduct{spQs clickBeacon spTags viewBeacon}showOptions showBuyNow quickShop quickShopCTALabel rewards{eligible state minQuantity rewardAmt promotionId selectionToken rewardMultiplierStr cbOffer term expiry description}promoData @include(if:$enablePromoData){type terms templateData{priceString imageUrl}}promoDiscount{discount discountEligible discountEligibleVariantPresent promotionId promoOffer state showOtherEligibleItemsCTA type min awardValue awardSubType maxPerTxn maxPerOrder tiers{awardValue minQuantity}}arExperiences{isARHome isZeekit isAROptical}eventAttributes{...GenericProductEventAttributesFragment}subscription{subscriptionEligible subscriptionTransactable}hasCarePlans petRx{eligible singleDispense}vision{ageGroup visionCenterApproved}showExploreOtherConditionsCTA isPreowned pglsCondition newConditionProductId preownedCondition keyAttributes{displayEnum value}mhmdFlag seeSimilar subscription{subscriptionEligible subscriptionTransactable showSubscriptionCTA}isSimilarLookEligible @include(if:$enableShopSimilarBottomSheet) winningProductId @include(if:$enableShopSimilarBottomSheet) orderLimit @include(if:$enableItemLimits) orderMinLimit @include(if:$enableItemLimits) canAddToList @include(if:$enableCanAddToList) isFreeWarranty @include(if:$enableIsFreeWarranty) isQSRItem isCustomizable}fragment GenericProductPriceInfoFragment on ProductPriceInfo{priceRange{minPrice maxPrice priceString}subscriptionDiscountPrice{priceString}currentPrice{...GenericProductPriceFragment priceDisplay}comparisonPrice{...GenericProductPriceFragment}wasPrice{...GenericProductPriceFragment}unitPrice{...GenericProductPriceFragment}listPrice{...GenericProductPriceFragment}savingsAmount{...GenericProductSavingsFragment}shipPrice{...GenericProductPriceFragment}additionalFees{dutyFee{price}}subscriptionPrice{priceString subscriptionString downPaymentString}priceDisplayCodes{priceDisplayCondition finalCostByWeight submapType isB2BPrice priceDisplayType}wPlusEarlyAccessPrice{memberPrice{...GenericProductPriceFragment}savings{...GenericProductSavingsFragment}eventStartTime eventStartTimeDisplay}subscriptionDualPrice subscriptionPercentage volumePriceTiers @include(if:$enableVolumePricing){currencyUnit minUnit price savingsAmount}taxInfo{isTaxable}}fragment GenericProductSavingsFragment on ProductSavings{amount percent priceString}fragment GenericProductPriceFragment on ProductPrice{price priceString variantPriceString priceType currencyUnit priceDisplay supportText}fragment GenericProductEventAttributesFragment on EventAttributes{priceFlip specialBuy}fragment GenericPreorderFragment on PreOrder{isPreOrder preOrderMessage preOrderStreetDateMessage streetDate streetDateDisplayable streetDateType releaseDate}fragment GenericVariantCriteriaFragment on VariantCriterion{name type id displayName isVariantTypeSwatch isVariantTypeAllowed variantList{id images name rank displayName swatchImageUrl availabilityStatus products selectedProduct{canonicalUrl usItemId}}}fragment GenericProductDiscountsFragment on Discounts{discountedValue{price priceString}discountMetaData{id type savings{amount priceString percent}price{price priceString priceDisplay}unitPrice{price priceString}comparisonPrice{price priceString}unitPriceDisplayCondition}}fragment GenericProductImageInfoFragment on ProductImageInfo{id name thumbnailUrl size allImages{id url type}}fragment GenericBadgeFragment on UnifiedBadge{groupsV2{name pos flow members{memType memId memStyleId content{...ContentV2Fragment}contentVariants:contentVariantsV2{pickup{...ContentV2Fragment}delivery{...ContentV2Fragment}shipping{...ContentV2Fragment}noIntent{...ContentV2Fragment}}}}}fragment ContentV2Fragment on ContentV2{type value styleId contDesc url actionId actionContent{type contentId value styleId}}fragment AddOnServicesFragment on AddOnService{serviceType serviceTitle serviceSubTitle serviceProviders groups{groupType groupTitle assetUrl shortDescription unavailabilityReason nearByStores{nodes{id displayName distance}}services{offerId}}}fragment GenericInGridMarqueeAdFragment on MarqueePlaceholder{__typename type moduleLocation lazy}fragment GenericInGridAdFragment on AdPlaceholder{__typename type moduleLocation lazy adUuid hasVideo hasAd moduleInfo videoAdType}fragment GenericTileTakeOverTileFragment on TileTakeOverProductPlaceholder{__typename type tileTakeOverTile{span title subtitle image{src alt assetId assetName}logoImage{src alt}backgroundColor titleTextColor subtitleTextColor tileCta{ctaLink{clickThrough{value}linkText title}ctaType ctaTextColor}adsEnabled adCardLocation enableLazyLoad}}fragment GenericTileTakeOverPrismFragment on PrismTileTakeOverProductPlaceholder{__typename type athModule locationPersonalized locationPinned moduleName moduleId moduleType zone viewType prismTileTakeOverTile{ad adCardLocation adsEnabled enableLazyLoad containerId personalizedAsset pinnedMessages disableContentPersonalization assetTypes metadata{pageNumber dwebPosition mobilePosition}asset{assetId assetType assetName assetLocaleId servedBy messageId configs{logo{image{assetId assetName src uid alt}}image{assetId assetName src uid alt}ctaLink{primaryCta{style textColor crossChannelLink{uid title linkText clickThrough{type webValue}}}secondaryCta{crossChannelLink{linkText title clickThrough{type webValue}uid}style textColor}}heading{text textColor}subheading{text textColor}backgroundColor}}}}fragment InlineCategoryNavigationFragment on InlineCategoryNavigationPlaceholder{__typename type}fragment EssCarouselFragment on ESSCarouselPlaceholder{__typename isLazy}fragment GenericPageMetaDataFragment on SearchInterface{pageMetadata{categoryNavigationMetaData{experienceType}storeSelectionHeader{fulfillmentMethodLabel storeDislayName}title canonical source description location{addressId}subscriptionEligible languageUrls @include(if:$enableSeoLangUrl){name url}noIndex}}fragment GenericPaginationFragment on SearchInterface{paginationV2{maxPage pageProperties}}fragment GenericRequestContextFragment on SearchInterface{requestContext{vertical hasGicIntent isFitmentFilterQueryApplied searchMatchType selectedFacetCount showComparisonCart categories{id name}}}fragment GenericErrorResponse on SearchInterface{errorResponse{correlationId source errorCodes errors{errorType statusCode statusMsg source}}}fragment GenericPillsModuleFragment on PillsSearchInterface{title titleColor:titleColorV1 url image:imageV1{src alt assetId assetName}}fragment BannerViewConfigFragment on BannerViewConfigCLS{title image imageAlt displayName description url urlAlt appStoreLink appStoreLinkAlt playStoreLink playStoreLinkAlt}fragment BannerModuleFragment on TempoWM_GLASSWWWSearchBannerConfigs{moduleType viewConfig{...BannerViewConfigFragment}}fragment PopularInBrowseFragment on TempoWM_GLASSWWWPopularInBrowseConfigs{seoBrowseRelmData(id:$catId){relm{id name url}}}fragment CopyBlockModuleFragment on TempoWM_GLASSWWWCopyBlockConfigs{copyBlock( facets:$rawFacet id:$catId marketSpecificParams:$marketSpecificParams ){cwc}}fragment GenericFacetFragment on Facet{title name expandOnLoad type displayType urlParams url layout min max selectedMin selectedMax unboundedMax stepSize isSelected valueDisplayLimit hasPopularValues popularValues{id title name expandOnLoad description type isSelected itemCount @include(if:$enableFacetCount) url baseSeoURL}values{id title name expandOnLoad description type itemCount @include(if:$enableFacetCount) url isSelected baseSeoURL catPathName @include(if:$enableAdditionalSearchDepartmentAnalytics) values{id title name expandOnLoad description type itemCount @include(if:$enableFacetCount) url isSelected baseSeoURL values{id title name expandOnLoad description type itemCount @include(if:$enableFacetCount) isSelected baseSeoURL values{id title name expandOnLoad description type itemCount @include(if:$enableFacetCount) isSelected baseSeoURL values{id title name expandOnLoad description type itemCount @include(if:$enableFacetCount) isSelected baseSeoURL values{id title name expandOnLoad description type itemCount @include(if:$enableFacetCount) isSelected baseSeoURL values{id title name expandOnLoad description type itemCount @include(if:$enableFacetCount) isSelected baseSeoURL values{id title name expandOnLoad description type itemCount @include(if:$enableFacetCount) isSelected baseSeoURL}}}}}}}}}fragment FitmentFragment on Fitments{partTypeIDs fitmentType isNarrowSearch fitmentOptionalFields{...FitmentFieldFragment}result{fitmentType status formId position quantityTitle spec{...FitmentSpecFragment}extendedAttributes{...FitmentFieldFragment}labels{...LabelFragment}resultSubTitle notes suggestions{...FitmentSuggestionFragment}oilChangeSchedulingInfo{formattedOilViscosity oilViscosity oilViscosityLabel formattedOilType oilType oilTypeLabel formattedOilCapacity oilCapacityQuarts oilCapacityLabel fittingOilFilters{brand manufacturerNumber}}}redirectUrl{title clickThrough{value}}labels{...LabelFragment}savedVehicle{vehicleId{...VehicleFieldFragment}vehicleType{...VehicleFieldFragment}vehicleYear{...VehicleFieldFragment}vehicleMake{...VehicleFieldFragment}vehicleModel{...VehicleFieldFragment}additionalAttributes{...VehicleFieldFragment}}fitmentFields{...VehicleFieldFragment}fitmentForms{id fields{...FitmentFieldFragment}title labels{...LabelFragment}garage{vehicles{...AutoVehicle}}}}fragment LabelFragment on FitmentLabels{ctas{...FitmentLabelEntityFragment}messages{...FitmentLabelEntityFragment}links{...FitmentLabelEntityFragment}images{...FitmentLabelEntityFragment}}fragment FitmentLabelEntityFragment on FitmentLabelEntity{id label}fragment VehicleFieldFragment on FitmentVehicleField{id label value}fragment FitmentSpecFragment on FitmentSpecValue{label displayValue}fragment FitmentFieldFragment on FitmentField{id displayName value extended data{value label}dependsOn isRequired displayForVehicleTypes errorMessage}fragment FitmentSuggestionFragment on FitmentSuggestion{id position loadIndex speedRating searchQueryParam labels{...LabelFragment}cat_id fitmentSuggestionParams{id value}optionalSuggestionParams{id value displayName data{label value}dependsOn isRequired errorMessage}applicationSuggestionParams{position}}fragment Hero4FragmentV2 on TempoWM_GLASSWWWHero4Configs{hero4DesktopImage:desktopImage{src}hero4MobileImage:mobileImage{alt src}hero4VerticalImagePosition:verticalImagePosition hero4HorizontalImagePosition:horizontalImagePosition hero4Eyebrow:eyebrow hero4Heading:heading{text textColor}subheading emphasizedText{text textColor}hero4CTA:primaryCTA{clickThrough{value}linkText}hero4AlertBanner:alertBanner{alertType title bodyCopy actionCta{uid title linkText clickThrough{value}}}bulletedList{bulletedIcon{alt src}bulletedText}additionalAssistance{text tertiaryCtaText tertiaryCtaType externalLink modalHeading modalBody}disclaimerText disclaimerCta{tertiaryCtaText tertiaryCtaType externalLink modalHeading modalBody}}fragment HeroPOVFragment on TempoWM_GLASSWWWHeroPovConfigsV1{autoRotation p13nCards:p13nCardsV1{...P13nHeroPOVCardFragment}povCards{card:cardV1{...CLSHeroPOVCardFragment}ad{adContent{data{...on TempoWM_GLASSWWWHeroPovConfigsCards{...HeroPOVCardFragment adJSON}}}}}}fragment CLSHeroPOVCardFragment on CLSTempoWM_GLASSWWWHeroPovConfigsCards{povStyle ctaButton{button{...TempoCommonLinkFragment}textColor ctaButtonBackgroundColor}heading{text textSize textColor textColorMobile textFontWeight}subheading{text textColor textColorMobile}image{mobileImage{...TempoCommonImageFragment}desktopImage{...TempoCommonImageFragment}}eyebrow{text textColor textColorMobile textFontWeight}detailsView{backgroundColor alignment isTransparent}links{link{...TempoCommonLinkFragment}textColor textColorMobile}legalDisclosure{regularText shortenedText textColor textColorMobile legalBottomSheetTitle legalBottomSheetDescription}sponsoredLabel{text textColor textColorMobile}logo{...TempoCommonImageFragment}enableLazyLoad adSlotPosition}fragment HeroPOVCardFragment on TempoWM_GLASSWWWHeroPovConfigsCards{povStyle ctaButton{button{...TempoCommonLinkFragment}textColor ctaButtonBackgroundColor}heading{text textSize textColor textColorMobile textFontWeight}subheading{text textColor textColorMobile}image{mobileImage{...TempoCommonImageFragment}desktopImage{...TempoCommonImageFragment}}eyebrow{text textColor textColorMobile textFontWeight}detailsView{backgroundColor alignment isTransparent}links{link{...TempoCommonLinkFragment}textColor textColorMobile}legalDisclosure{regularText shortenedText textColor textColorMobile legalBottomSheetTitle legalBottomSheetDescription}sponsoredLabel{text textColor textColorMobile}logo{...TempoCommonImageFragment}enableLazyLoad}fragment TempoCommonImageFragment on TempoCommonImage{src alt assetId assetName uid clickThrough{value}}fragment TempoCommonLinkFragment on TempoCommonStringLink{linkText title uid clickThrough{value}}fragment P13nHeroPOVCardFragment on CLETempoWM_GLASSWWWHeroPovConfigsCards{povStyle ctaButton{button{...TempoCommonLinkFragment}textColor ctaButtonBackgroundColor}heading{text textSize textColor textColorMobile textFontWeight}subheading{text textColor textColorMobile}image{mobileImage{...TempoCommonImageFragment}desktopImage{...TempoCommonImageFragment}}eyebrow{text textColor textColorMobile textFontWeight}detailsView{backgroundColor alignment isTransparent}links{link{...TempoCommonLinkFragment}textColor textColorMobile}legalDisclosure{regularText shortenedText textColor textColorMobile legalBottomSheetTitle legalBottomSheetDescription}sponsoredLabel{text textColor textColorMobile}logo{...TempoCommonImageFragment}enableLazyLoad}fragment InlineSearchModuleFragment on TempoWM_GLASSWWWInlineSearchConfigs{headingText placeholderText headingTextColor}fragment MarqueeDisplayAdConfigsFragment on TempoWM_GLASSWWWMarqueeDisplayAdConfigs{_rawConfigs ad{...DisplayAdFragment}}fragment DisplayAdFragment on Ad{...AdFragment adContent{type data{__typename...AdDataDisplayAdFragment...AdDataDisplayAdDSPFragment}}}fragment AdFragment on Ad{status moduleType platform pageId pageType storeId stateCode zipCode pageContext moduleConfigs adsContext adRequestComposite}fragment AdDataDisplayAdFragment on AdData{...on DisplayAd{json status}}fragment AdDataDisplayAdDSPFragment on AdData{...on MultiImpDspAd{ads{assets eventTrackers link metaData templateId variantId availableVariantIds}}...on DisplayAdDSP{assets eventTrackers link metaData templateId variantId availableVariantIds}}fragment SkylineDisplayAdConfigsFragment on TempoWM_GLASSWWWSkylineDisplayAdConfigs{_rawConfigs ad{...SkylineDisplayAdFragment}}fragment SkylineDisplayAdFragment on Ad{...SkylineAdFragment adContent{type data{__typename...SkylineAdDataDisplayAdFragment...SkylineAdDataDisplayAdDSPFragment}}}fragment SkylineAdFragment on Ad{status moduleType platform pageId pageType storeId stateCode zipCode pageContext moduleConfigs adsContext adRequestComposite}fragment SkylineAdDataDisplayAdFragment on AdData{...on DisplayAd{json status}}fragment SkylineAdDataDisplayAdDSPFragment on AdData{...on MultiImpDspAd{ads{assets eventTrackers link metaData templateId variantId availableVariantIds}}...on DisplayAdDSP{assets eventTrackers link metaData templateId variantId availableVariantIds}}fragment GalleryDisplayAdConfigsFragment on TempoWM_GLASSWWWGalleryDisplayAdConfigs{_rawConfigs}fragment DynamicAdContainerConfigsFragment on TempoWM_GLASSWWWDynamicAdContainerConfigs{_rawConfigs adModules{moduleType moduleLocation priority title viewAgainLogo viewAgainText viewAgainCTA}zoneLocation lazy}fragment MosaicGridFragment on TempoWM_GLASSWWWMosaicGridConfigs{paginationEnabled backgroundColor dWebGridStartingDirection backgroundImage{src alt assetId assetName}tabList{tabName shelfId initialDisplaySize}pillList{pillName pillUrl{title clickThrough{value}}}expandCollapseDetails{collapsedStateItemCount collapsedStateButtonTitle expandedStateButtonTitle}mosaicPageType bannerList{backgroundColor titleDetails{title titleColor fontType}subTitleDetails{subTitle subTitleColor fontType}ctaDetails{ctaTitle ctaTextColor ctaLink ctaType}mwebBackgroundImage{src alt assetId assetName}dwebBackgroundImage{src alt assetId assetName}}placeholderTile{backgroundColor titleDetails{title titleColor fontType}ctaDetails{ctaTitle ctaTextColor ctaLink ctaType}span1BackgroundImage{src alt}span2BackgroundImage{src alt}}footerDetails{backgroundColor titleDetails{title titleColor fontType}subTitleDetails{subTitle subTitleColor fontType}ctaDetails{ctaTitle ctaTextColor ctaLink ctaType}mwebBackgroundImage{src alt}dwebBackgroundImage{src alt}}headerDetails{titleDetails{title titleColor fontType titleAlignment}subTitleDetails{subTitle subTitleColor fontType titleAlignment}}tileTakeOverList{...TileTakeOverListFragment}mixedResults{__typename...on TempoWM_GLASSWWWMosaicGridConfigsTileTakeOverList{...TileTakeOverListFragment}...on TempoWM_GLASSWWWMosaicGridConfigsBannerList{...BannerListFragment}}dealsMosaic(searchParams:$searchParams){...GenericItemStacksFragment...GenericPaginationFragment...GenericErrorResponse}}fragment TileTakeOverListFragment on TempoWM_GLASSWWWMosaicGridConfigsTileTakeOverList{__typename backgroundColor mWebBackgroundImage{src}dWebBackgroundImage{src}tileTakeOverGroupPosition headlineDetails{headline headlineColor fontType}subheadDetails{subhead subHeadColor fontType}tileCta{ctaStyle ctaType ctaTypeMoreInfo{moreInfoTitle moreInfoDescription moreInfoLink{linkText title clickThrough{value rawValue}}}ctaLink{linkText title clickThrough{value rawValue}}ctaTextColor ctaPosition}}fragment BannerListFragment on TempoWM_GLASSWWWMosaicGridConfigsBannerList{__typename backgroundColor mwebBackgroundImage{alt src}dwebBackgroundImage{alt src}titleDetails{title titleColor fontType}subTitleDetails{subTitle subTitleColor fontType}ctaDetails{ctaTitle ctaLink ctaTextColor ctaType}}fragment HorizontalChipModuleConfigsFragment on TempoWM_GLASSWWWHorizontalChipModuleConfigs{chipModuleSource:moduleSource chipHeading:heading headingColor backgroundImage{src alt}backgroundColor desktopImageHeight desktopImageWidth mobileImageHeight mobileImageWidth chipModule{title url{linkText title clickThrough{type value}}}chipModuleWithImages{title titleColor url{linkText title clickThrough{type value}}image{assetId assetName alt clickThrough{type value}height src title width}}}fragment SkinnyBannerFragment on TempoWM_GLASSWWWSkinnyBannerConfigs{campaignsV1{bannerType desktopBannerHeight bannerImage{src title alt assetId assetName}mobileBannerHeight mobileImage{src title alt assetId assetName}clickThroughUrl{clickThrough{value}}backgroundColor heading{title fontColor}subHeading{title fontColor}bannerCta{ctaLink{linkText clickThrough{value}}textColor ctaType}}}fragment SkinnyBannerConfigsUnifiedFragment on SkinnyBannerConfigs{campaignsV2{bannerTypeV2:bannerType desktopBannerHeight bannerImage{src title alt assetId assetName}mobileBannerHeight signedOutCta{title linkText}promoLegalDisclaimer mobileImage{src title alt assetId assetName}clickThroughUrl{clickThrough{value}}backgroundColor heading{title fontColor}subHeading{title fontColor}bannerCtaV2:bannerCta{ctaLink{linkText clickThrough{value}}textColor ctaType}}}fragment TileTakeOverProductFragment on TempoWM_GLASSWWWTileTakeOverProductConfigs{dwebSlots mwebSlots overrideDefaultTiles TileTakeOverProductDetailsV1{pageNumber span dwebPosition mwebPosition title subtitle image{src alt assetId assetName}logoImage{src alt}backgroundColor titleTextColor subtitleTextColor tileCta{ctaLink{clickThrough{value}linkText title uid}ctaType ctaTextColor}adsEnabled adCardLocation enableLazyLoad}}fragment TileTakeOverProductUnifiedFragment on TileTakeOverProductConfigs{dwebSlots mwebSlots overrideDefaultTiles tileTakeOverProductDetailsV1Unified:TileTakeOverProductDetailsV1{pageNumber span dwebPosition mwebPosition title subtitle image{src alt assetId assetName}logoImage{src alt}backgroundColor titleTextColor subtitleTextColor tileCta{ctaLink{clickThrough{value}linkText title uid}ctaType ctaTextColor}adsEnabled adCardLocation enableLazyLoad}}fragment PrismTileTakeOverFragment on TempoWM_GLASSWWWPrismTileTakeOverConfigsV1{locationPinned locationPersonalized athModule viewType metadata{dwebSlots mobileSlots}prismTileTakeOverContainers{...PrismTileTakeOverContainerFragment}}fragment PrismTileTakeOverContainerFragment on PrismTileTakeOverContainer{__typename containerId personalizedAsset pinnedMessages disableContentPersonalization assetTypes metadata{pageNumber dwebPosition mobilePosition}asset{assetId assetType assetName assetLocaleId servedBy messageId configs{logo{image{assetId assetName src uid alt}}image{assetId assetName src uid alt}ctaLink{primaryCta{style textColor crossChannelLink{uid title linkText clickThrough{type webValue}}}secondaryCta{crossChannelLink{linkText title clickThrough{type webValue}uid}style textColor}}heading{text textColor}subheading{text textColor}backgroundColor}}}fragment TileDisplayAdFragment on TempoWM_GLASSWWWTileDisplayAdConfigs{_rawConfigs dwebSlots mwebSlots TileDisplayAdCardDetails{...on TempoWM_GLASSWWWTileDisplayAdConfigsTileDisplayAdCardDetails{moduleLocation lazy pageNumber span dwebPosition mwebPosition clientCapabilities ad{adContent{data{...on DisplayAd{json}...on DisplayAdDSP{assets eventTrackers link metaData templateId variantId availableVariantIds}}}adRequestComposite adsContext moduleType pageContext stateCode status storeId zipCode}}}}fragment TopNavFragment on TempoWM_GLASSWWWCategoryTopNavConfigs{navHeaders{header{linkText clickThrough{value}}headerImageGroup{headerImage{alt src assetName assetId}imgTitle imgSubText imgLink{linkText title clickThrough{value}}}categoryGroup{category{linkText clickThrough{value}}startNewColumn subCategoryGroup{subCategory{linkText clickThrough{value}}isBold openInNewTab}}}configsForMWeb{bannerBackgroundColor bannerTextColor showAsBannerInMWeb}}fragment EnhancedCategoryNavFragment on TempoWM_GLASSWWWEnhancedCategoryNavConfigs{categoryHeaderGroup{headerName headerActionLink{linkText clickThrough{value}}showPipeSeparator columnGroup{categoryGroup{categoryLink{linkText clickThrough{value}}categoryImage{alt src assetName assetId title clickThrough{value}}subCategoryGroup{subCategory{linkText clickThrough{value}}}}}}styleConfig{bannerBackgroundColor bannerTextColor headerAlignment showAsBannerInMWeb}}fragment AlertBannerListFragment on TempoSAMS_GLASSWWWAlertBannerListConfigs{AlertBannerList{message type actionCta{title clickThrough{type value}}}}fragment BrandAmplifierAdConfigs on TempoWM_GLASSWWWBrandAmplifierAdConfigs{_rawConfigs moduleLocation ad @skip(if:$fungibilityEnabled){...SponsoredBrandsAdFragment}adV1 @include(if:$fungibilityEnabled){...SponsoredBrandsVideoAdFragment}}fragment SponsoredBrandsAdFragment on Ad{...AdFragment adContent{type data @skip(if:$fetchDataV1){__typename...AdDataSponsoredBrandsFragment}dataV1 @include(if:$fetchDataV1){__typename...AdDataSponsoredBrandsV1Fragment}}}fragment AdDataSponsoredBrandsFragment on AdData{...on SponsoredBrands{adUuid adExpInfo moduleInfo brands{logo{featuredHeadline featuredImage featuredImageName featuredUrl logoClickTrackUrl}products{...ProductFragment}}}}fragment AdDataSponsoredBrandsV1Fragment on AdData{...on SponsoredBrandsV1{adUuid adExpInfo moduleInfo brands{logo{featuredHeadline featuredImage featuredImageName featuredUrl logoClickTrackUrl}products{...ProductFragment}customInfo{images}}}}fragment ProductFragment on Product{usItemId offerId specialCtaType @include(if:$enableSignInToSeePrice) orderMinLimit @include(if:$enableItemLimits) orderLimit @include(if:$enableItemLimits) badges{flags{__typename...on BaseBadge{id text key query type styleId}...on PreviouslyPurchasedBadge{id text key lastBoughtOn numBought criteria{name value}}}labels{__typename...on BaseBadge{id text key}...on PreviouslyPurchasedBadge{id text key lastBoughtOn numBought}}tags{__typename...on BaseBadge{id text key}}groups{__typename name members{...on BadgeGroupMember{__typename id key memberType rank slaText styleId text textTemplate @include(if:$enableAdsTemplateBadging) textValues @include(if:$enableAdsTemplateBadging) type}...on CompositeGroupMember{__typename join memberType styleId suffix members{__typename id key memberType rank slaText styleId text textTemplate @include(if:$enableAdsTemplateBadging) textValues @include(if:$enableAdsTemplateBadging) type}}}}groupsV2{name pos flow members{memType memId memStyleId content{type value styleId contDesc url actionId actionContent{type contentId value styleId}}}}}priceInfo{priceDisplayCodes{rollback reducedPrice eligibleForAssociateDiscount clearance strikethrough submapType priceDisplayCondition unitOfMeasure pricePerUnitUom}currentPrice{price priceString priceDisplay}wasPrice{price priceString}listPrice{price priceString}priceRange{minPrice maxPrice priceString}unitPrice{price priceString}savingsAmount{amount priceString}comparisonPrice{priceString}subscriptionPrice{priceString subscriptionString price minPrice maxPrice intervalFrequency duration percentageRate durationUOM interestUOM downPaymentString}subscriptionDiscountPrice{priceString}wPlusEarlyAccessPrice{memberPrice{price priceString priceDisplay}savings{amount priceString}eventStartTime eventStartTimeDisplay}}preOrder{streetDate streetDateDisplayable streetDateType isPreOrder preOrderMessage preOrderStreetDateMessage}annualEventV2 earlyAccessEvent isEarlyAccessItem eventAttributes{priceFlip specialBuy}snapEligible showOptions promoData @include(if:$enableAdsPromoData){type templateData{priceString imageUrl}}sponsoredProduct{spQs clickBeacon spTags}subscription{subscriptionEligible showSubscriptionCTA subscriptionTransactable}canonicalUrl conditionV2{code groupCode}numberOfReviews averageRating availabilityStatus imageInfo{thumbnailUrl allImages{id url}}name fulfillmentBadge classType type showAtc brand sellerId sellerName sellerType rxDrugScheduleType @include(if:$enableRxDrugScheduleModal)}fragment SponsoredBrandsVideoAdFragment on Ad{...AdFragment adContent{type selectedModuleType dataV1 @skip(if:$fetchDataV2){__typename...AdDataSponsoredBrandsV1Fragment...AdDataSponsoredVideoFragment}dataV2 @include(if:$fetchDataV2){__typename...AdDataSponsoredBrandsV1Fragment...AdDataSponsoredVideoV1Fragment}}}fragment AdDataSponsoredVideoFragment on AdData{...on SponsoredVideos{adUuid adExpInfo moduleInfo videos{video{vastXml thumbnail spqs}products{...ProductFragment}}}}fragment AdDataSponsoredVideoV1Fragment on AdData{...on SponsoredVideosV1{adUuid adExpInfo moduleInfo videos{video{vastXml thumbnail spqs}products{...ProductFragment}logo{featuredImage featuredImageName featuredUrl featuredHeadline logoClickTrackUrl}}}}fragment AutoVehicle on AutoVehicle{cid color default documentType fitment{baseBodyType baseVehicleId driveType{id name}engineOptions{id isSelected label}smartSubModel tireSizeOptions{diameter isCustom isSelected loadIndex positions ratio speedRating tirePressureFront tirePressureRear tireSize width}trim}isDually licensePlate licensePlateState licensePlateStateCode make model reminders{id}source sourceType subModel{subModelId subModelName}subModelOptions{subModelId subModelName}vehicleId vehicleType vin year}fragment GenericSeoFaqFragment on TempoWM_GLASSWWWGenericSEOFAQModuleConfigs{seoFaqList:faqList(id:$catId pageType:$pageType){seoFaqQuestion:questionText seoFaqAnswer:answerParagraphs}}fragment SponsoredVideoAdFragment on TempoWM_GLASSWWWSponsoredVideoAdConfigs{__typename sponsoredVideoAd{ad{adContent{data{...on SponsoredVideos{adUuid hasVideo moduleInfo}}}}}}fragment GenericSortAndFilterModule on _TempoWM_GLASSWWWSearchSortFilterModuleConfigs{facetsV1 @skip(if:$enablePortableFacets){...GenericFacetFragment}topNavFacets{...GenericFacetFragment}allSortAndFilterFacets{...GenericFacetFragment}sortByColor enableSearchSortFilterReposition}fragment ImageBannerCarouselFragment on TempoSAMS_GLASSWWWImageBannerCarouselConfigs{imageBannerAutoRotation:autoRotation desktopBannerHeight mobileBannerHeight image{desktopImage{src title alt assetId assetName}mobileImage{src title alt assetId assetName}clickThroughUrl{clickThrough{value}}}}fragment SimpleEmailSignUpFragment on TempoWM_GLASSWWWSimpleEmailSignUpConfigs{simpleEmailContent{contentPosition textAlign fontSize textPartsType{text bold url lineBreak}}simpleEmailBannerImages{imagePosition imageType{src alt width height uid}}simpleEmailBackgroundColor}fragment FaqFragment on TempoWM_GLASSWWWFAQConfigs{title faqList{questionText answerParagraphs{paragraph}}}fragment AdPlaceholderModuleConfigsFragment on TempoWM_GLASSWWWAdPlaceholderModuleConfigs{modulePlacementConfig{moduleLocation modules cache}dedupe adFungibility{ad{__typename...AdFragment adContentV1{selectedModuleType selectedModuleLocation type hasData __typename dataV1 @skip(if:$fetchDataV2){__typename...AdDataSponsoredBrandsV1Fragment...AdDataSponsoredVideoFragment}dataV2 @include(if:$fetchDataV2){__typename...AdDataSponsoredBrandsV1Fragment...AdDataSponsoredVideoV1Fragment}}}}}',
            'variables': {
                'id': '',
                'dealsId': '',
                'query': '',
                'nudgeContext': '',
                'page': 1,
                'prg': 'desktop',
                'catId': self.cat_id,
                'facet': '',
                'sort': self.sort,
                'rawFacet': '',
                'seoPath': '',
                'ps': 44,
                'limit': 40,
                'ptss': '',
                'trsp': '',
                'beShelfId': '',
                'recall_set': '',
                'module_search': '',
                'min_price': '',
                'max_price': '',
                'storeSlotBooked': '',
                'additionalQueryParams': {
                    'hidden_facet': None,
                    'translation': None,
                    'isMoreOptionsTileEnabled': True,
                    'rootDimension': '',
                    'altQuery': '',
                    'selectedFilter': '',
                    'neuralSearchSeeAll': False,
                    'isLMPBrowsePage': False,
                },
                'searchArgs': {
                    'query': '',
                    'cat_id': self.cat_id,
                    'prg': 'desktop',
                    'facet': '',
                },
                'enableCopyBlock': True,
                'enableVariantCount': False,
                'enableSlaBadgeV2': False,
                'enableUnifiedProductFragment': False,
                'enableESSCarousel': False,
                'fitmentFieldParams': {
                    'powerSportEnabled': True,
                    'dynamicFitmentEnabled': True,
                    'extendedAttributesEnabled': False,
                    'extendedAttributesV2Enabled': False,
                    'fuelTypeEnabled': False,
                },
                'fitmentSearchParams': {
                    'id': '',
                    'dealsId': '',
                    'query': '',
                    'nudgeContext': '',
                    'page': 1,
                    'prg': 'desktop',
                    'catId': self.cat_id,
                    'facet': '',
                    'sort': self.sort,
                    'rawFacet': '',
                    'seoPath': '',
                    'ps': 40,
                    'limit': 40,
                    'ptss': '',
                    'trsp': '',
                    'beShelfId': '',
                    'recall_set': '',
                    'module_search': '',
                    'min_price': '',
                    'max_price': '',
                    'storeSlotBooked': '',
                    'additionalQueryParams': {
                        'hidden_facet': None,
                        'translation': None,
                        'isMoreOptionsTileEnabled': True,
                        'rootDimension': '',
                        'altQuery': '',
                        'selectedFilter': '',
                        'neuralSearchSeeAll': False,
                        'isLMPBrowsePage': False,
                    },
                    'searchArgs': {
                        'query': '',
                        'cat_id': self.cat_id,
                        'prg': 'desktop',
                        'facet': '',
                    },
                    'enableCopyBlock': True,
                    'enableVariantCount': False,
                    'enableSlaBadgeV2': False,
                    'enableUnifiedProductFragment': False,
                    'enableESSCarousel': False,
                    'cat_id': self.cat_id,
                    '_be_shelf_id': '',
                },
                'searchParams': {
                    'id': '',
                    'dealsId': '',
                    'query': '',
                    'nudgeContext': '',
                    'page': 1,
                    'prg': 'desktop',
                    'catId': self.cat_id,
                    'facet': '',
                    'sort': self.sort,
                    'rawFacet': '',
                    'seoPath': '',
                    'ps': 40,
                    'limit': 40,
                    'ptss': '',
                    'trsp': '',
                    'beShelfId': '',
                    'recall_set': '',
                    'module_search': '',
                    'min_price': '',
                    'max_price': '',
                    'storeSlotBooked': '',
                    'additionalQueryParams': {
                        'hidden_facet': None,
                        'translation': None,
                        'isMoreOptionsTileEnabled': True,
                        'rootDimension': '',
                        'altQuery': '',
                        'selectedFilter': '',
                        'neuralSearchSeeAll': False,
                        'isLMPBrowsePage': False,
                    },
                    'searchArgs': {
                        'query': '',
                        'cat_id': self.cat_id,
                        'prg': 'desktop',
                        'facet': '',
                    },
                    'enableCopyBlock': True,
                    'enableVariantCount': False,
                    'enableSlaBadgeV2': False,
                    'enableUnifiedProductFragment': False,
                    'enableESSCarousel': False,
                    'cat_id': self.cat_id,
                    '_be_shelf_id': '',
                },
                'enableFashionTopNav': False,
                'fetchMarquee': True,
                'fetchSkyline': True,
                'fetchSbaTop': True,
                'fetchDataV1': False,
                'fetchDataV2': False,
                'fungibilityEnabled': False,
                'fetchGallery': False,
                'fetchDac': False,
                'enablePortableFacets': True,
                'tenant': 'CHILE_EA_GLASS',
                'pageType': 'BrowsePage',
                'enableFacetCount': True,
                'marketSpecificParams': '{"banner":"ea","pageType":"browse","locale":"es_CL"}',
                'enableMultiSave': False,
                'enableInStoreShelfMessage': False,
                'fSeo': True,
                'enableSellerType': False,
                'enableItemRank': False,
                'enableOptimisticWeightUpdate': False,
                'enableFulfillmentTagsEnhacements': False,
                'enableRxDrugScheduleModal': False,
                'enablePromoData': True,
                'enableAdsPromoData': False,
                'enableSeoLangUrl': False,
                'enableImageBannerCarousel': False,
                'enableHero4': False,
                'enableSeoBrowseMetaDataShortDesc': False,
                'enableCanAddToList': False,
                'enablePromotionMessages': False,
                'enableDebugAnalyticsTags': False,
                'enableSignInToSeePrice': False,
                'enableSimpleEmailSignUp': False,
                'enableModuleReposition': False,
                'enableUnifiedSchema': False,
                'version': 'v1',
                'postProcessingVersion': 1,
            },
        }
        self.url = f'https://www.lider.cl/orchestra/graphql/browse?page=1&prg=desktop&catId={self.cat_id}&sort={self.sort}&ps=44&limit=40&additionalQueryParams.isMoreOptionsTileEnabled=true&additionalQueryParams.isGenAiEnabled=undefined&additionalQueryParams.view_module=undefined&additionalQueryParams.search_ctx=undefined&additionalQueryParams.neuralSearchSeeAll=false&additionalQueryParams.isModuleArrayReq=undefined&additionalQueryParams.isLMPBrowsePage=false&searchArgs.cat_id={self.cat_id}&searchArgs.prg=desktop&enableDesktopHighlights=undefined&enableVolumePricing=undefined&enableCopyBlock=true&enableVariantCount=false&enableSlaBadgeV2=false&enableUnifiedProductFragment=false&enableESSCarousel=false&fitmentFieldParams=true_true_false_false_false&searchParams.page=1&searchParams.prg=desktop&searchParams.catId={self.cat_id}&searchParams.sort={self.sort}&searchParams.ps=40&searchParams.limit=40&searchParams.additionalQueryParams.isMoreOptionsTileEnabled=true&searchParams.additionalQueryParams.isGenAiEnabled=undefined&searchParams.additionalQueryParams.view_module=undefined&searchParams.additionalQueryParams.search_ctx=undefined&searchParams.additionalQueryParams.neuralSearchSeeAll=false&searchParams.additionalQueryParams.isModuleArrayReq=undefined&searchParams.additionalQueryParams.isLMPBrowsePage=false&searchParams.searchArgs.cat_id={self.cat_id}&searchParams.searchArgs.prg=desktop&searchParams.enableDesktopHighlights=undefined&searchParams.enableVolumePricing=undefined&searchParams.enableCopyBlock=true&searchParams.enableVariantCount=false&searchParams.enableSlaBadgeV2=false&searchParams.enableUnifiedProductFragment=false&searchParams.enableESSCarousel=false&searchParams.cat_id={self.cat_id}&enableFashionTopNav=false&fetchMarquee=true&fetchSkyline=true&fetchSbaTop=true&fetchDataV1=false&fetchDataV2=false&fungibilityEnabled=false&fetchGallery=false&fetchDac=false&enablePortableFacets=true&tenant=CHILE_EA_GLASS&pageType=BrowsePage&enableFacetCount=true&marketSpecificParams={{"banner":"ea","pageType":"browse","locale":"es_CL"}}&enableMultiSave=false&enableInStoreShelfMessage=false&fSeo=true&enableSellerType=false&enableItemRank=false&enableOptimisticWeightUpdate=false&enableFulfillmentTagsEnhacements=false&enableRxDrugScheduleModal=false&enablePromoData=true&enableAdsPromoData=false&enableSeoLangUrl=false&enableImageBannerCarousel=false&enableHero4=false&enableSeoBrowseMetaDataShortDesc=false&enableCanAddToList=false&enablePromotionMessages=false&enableDebugAnalyticsTags=false&enableSignInToSeePrice=false&enableSimpleEmailSignUp=false&enableModuleReposition=false&enableUnifiedSchema=false&version=v1&postProcessingVersion=1'

    def scrape(self):
        all_products = []
        page = 1
        has_more = True

        while has_more:
            print(f"[PAGINA] Scrapeando pagina {page} de Lider (Cat: {self.cat_id})...")
            
            # Actualizamos la página en el JSON y en la URL (opcional si solo usa POST)
            self.json_data['variables']['page'] = page
            # Si el sitio requiere la página en la URL también:
            current_url = self.url.replace('page=1', f'page={page}')

            try:
                response = requests.post(
                    current_url,
                    cookies=self.cookies,
                    headers=self.headers,
                    json=self.json_data,
                    timeout=30
                )
                
                if response.status_code != 200:
                    print(f"[ERROR] En la peticion (Status {response.status_code})")
                    print(f"[DEBUG] Respuesta del servidor: {response.text[:500]}") # Ver los primeros 500 caracteres
                    break

                data = response.json()
                
                # Navegar por el JSON de Lider para encontrar los items
                search_data = data.get('data', {}).get('search', {})
                item_stacks = search_data.get('searchResult', {}).get('itemStacks', [])
                
                if not item_stacks:
                    print("[FIN] No se encontraron mas productos.")
                    break

                page_products = []
                for stack in item_stacks:
                    items = stack.get('itemsV2', [])
                    for item in items:
                        # Filtrar solo por tipo 'Product' para evitar banners publicitarios
                        if item.get('__typename') != 'Product':
                            continue
                            
                        name = item.get('name')
                        price_info = item.get('priceInfo', {})
                        current_price = price_info.get('currentPrice', {}).get('price', 0)
                        
                        # Extraer ID externo y URL
                        external_id = item.get('id')
                        item_url = item.get('canonicalUrl', '')
                        if item_url and not item_url.startswith('http'):
                            item_url = f"https://www.lider.cl{item_url}"
                        
                        # Vendedor
                        seller = item.get('sellerName', 'Lider')

                        page_products.append({
                            "external_id": external_id,
                            "name": name,
                            "price": current_price,
                            "url": item_url,
                            "seller": seller,
                            "category": self.cat_id  # Guardamos el ID de categoría usado
                        })

                if not page_products:
                    has_more = False
                else:
                    all_products.extend(page_products)
                    # Verificar si hay más páginas según el conteo total (opcional)
                    # O simplemente seguir hasta que no vengan items
                    page += 1
                    # Pausa aleatoria para evitar detección
                    import random
                    time.sleep(random.uniform(2, 5))

            except Exception as e:
                print(f"❌ Error durante el scrape: {e}")
                break

        return all_products
