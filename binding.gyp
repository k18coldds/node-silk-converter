{
  "variables": {
      "libdir%":"internal",
      "silk_libname%":"silk_converter"
  },
  "targets": [
    {
      "target_name": "<(module_name)",
      "include_dirs": ["<!(node -e \"require('nan')\")"],
      "conditions": [
        ["libdir != 'internal'", {
            "include_dirs": [ "<(libdir)/include" ],
            "libraries": [
               "-l<(silk_libname)"
            ],
            "conditions": [ [ "OS=='linux'", {"libraries+":["-Wl,-rpath=<@(libdir)/lib"]} ] ],
            "conditions": [ [ "OS!='win'", {"libraries+":["-L<@(libdir)/lib"]} ] ],
            'msvs_settings': {
              'VCLinkerTool': {
                'AdditionalLibraryDirectories': [
                  '<(libdir)/lib'
                ],
              },
            }
        },
        {
            "dependencies": [
            ]
        }
        ]
      ],
      "sources": [
        "src/silk.cc",
        "src/Decoder.c","src/Encoder.c",
        "src/src/SKP_Silk_A2NLSF.c","src/src/SKP_Silk_CNG.c","src/src/SKP_Silk_HP_variable_cutoff_FIX.c","src/src/SKP_Silk_LBRR_reset.c","src/src/SKP_Silk_LPC_inv_pred_gain.c","src/src/SKP_Silk_LPC_synthesis_filter.c","src/src/SKP_Silk_LPC_synthesis_order16.c","src/src/SKP_Silk_LP_variable_cutoff.c","src/src/SKP_Silk_LSF_cos_table.c","src/src/SKP_Silk_LTP_analysis_filter_FIX.c","src/src/SKP_Silk_LTP_scale_ctrl_FIX.c","src/src/SKP_Silk_MA.c","src/src/SKP_Silk_NLSF2A.c","src/src/SKP_Silk_NLSF2A_stable.c","src/src/SKP_Silk_NLSF_MSVQ_decode.c","src/src/SKP_Silk_NLSF_MSVQ_encode_FIX.c","src/src/SKP_Silk_NLSF_VQ_rate_distortion_FIX.c","src/src/SKP_Silk_NLSF_VQ_sum_error_FIX.c","src/src/SKP_Silk_NLSF_VQ_weights_laroia.c","src/src/SKP_Silk_NLSF_stabilize.c","src/src/SKP_Silk_NSQ.c","src/src/SKP_Silk_NSQ_del_dec.c","src/src/SKP_Silk_PLC.c","src/src/SKP_Silk_VAD.c","src/src/SKP_Silk_VQ_nearest_neighbor_FIX.c","src/src/SKP_Silk_ana_filt_bank_1.c","src/src/SKP_Silk_apply_sine_window.c","src/src/SKP_Silk_array_maxabs.c","src/src/SKP_Silk_autocorr.c","src/src/SKP_Silk_biquad.c","src/src/SKP_Silk_biquad_alt.c","src/src/SKP_Silk_burg_modified.c","src/src/SKP_Silk_bwexpander.c","src/src/SKP_Silk_bwexpander_32.c","src/src/SKP_Silk_code_signs.c","src/src/SKP_Silk_control_audio_bandwidth.c","src/src/SKP_Silk_control_codec_FIX.c","src/src/SKP_Silk_corrMatrix_FIX.c","src/src/SKP_Silk_create_init_destroy.c","src/src/SKP_Silk_dec_API.c","src/src/SKP_Silk_decode_core.c","src/src/SKP_Silk_decode_frame.c","src/src/SKP_Silk_decode_parameters.c","src/src/SKP_Silk_decode_pitch.c","src/src/SKP_Silk_decode_pulses.c","src/src/SKP_Silk_decoder_set_fs.c","src/src/SKP_Silk_detect_SWB_input.c","src/src/SKP_Silk_div_oabi.c","src/src/SKP_Silk_enc_API.c","src/src/SKP_Silk_encode_frame_FIX.c","src/src/SKP_Silk_encode_parameters.c","src/src/SKP_Silk_encode_pulses.c","src/src/SKP_Silk_find_LPC_FIX.c","src/src/SKP_Silk_find_LTP_FIX.c","src/src/SKP_Silk_find_pitch_lags_FIX.c","src/src/SKP_Silk_find_pred_coefs_FIX.c","src/src/SKP_Silk_gain_quant.c","src/src/SKP_Silk_init_encoder_FIX.c","src/src/SKP_Silk_inner_prod_aligned.c","src/src/SKP_Silk_interpolate.c","src/src/SKP_Silk_k2a.c","src/src/SKP_Silk_k2a_Q16.c","src/src/SKP_Silk_lin2log.c","src/src/SKP_Silk_log2lin.c","src/src/SKP_Silk_noise_shape_analysis_FIX.c","src/src/SKP_Silk_pitch_analysis_core.c","src/src/SKP_Silk_pitch_est_tables.c","src/src/SKP_Silk_prefilter_FIX.c","src/src/SKP_Silk_process_NLSFs_FIX.c","src/src/SKP_Silk_process_gains_FIX.c","src/src/SKP_Silk_quant_LTP_gains_FIX.c","src/src/SKP_Silk_range_coder.c","src/src/SKP_Silk_regularize_correlations_FIX.c","src/src/SKP_Silk_resampler.c","src/src/SKP_Silk_resampler_down2.c","src/src/SKP_Silk_resampler_down2_3.c","src/src/SKP_Silk_resampler_down3.c","src/src/SKP_Silk_resampler_private_AR2.c","src/src/SKP_Silk_resampler_private_ARMA4.c","src/src/SKP_Silk_resampler_private_IIR_FIR.c","src/src/SKP_Silk_resampler_private_copy.c","src/src/SKP_Silk_resampler_private_down4.c","src/src/SKP_Silk_resampler_private_down_FIR.c","src/src/SKP_Silk_resampler_private_up2_HQ.c","src/src/SKP_Silk_resampler_private_up4.c","src/src/SKP_Silk_resampler_rom.c","src/src/SKP_Silk_resampler_up2.c","src/src/SKP_Silk_residual_energy16_FIX.c","src/src/SKP_Silk_residual_energy_FIX.c","src/src/SKP_Silk_scale_copy_vector16.c","src/src/SKP_Silk_scale_vector.c","src/src/SKP_Silk_schur.c","src/src/SKP_Silk_schur64.c","src/src/SKP_Silk_shell_coder.c","src/src/SKP_Silk_sigm_Q15.c","src/src/SKP_Silk_solve_LS_FIX.c","src/src/SKP_Silk_sort.c","src/src/SKP_Silk_sum_sqr_shift.c","src/src/SKP_Silk_tables_LTP.c","src/src/SKP_Silk_tables_NLSF_CB0_10.c","src/src/SKP_Silk_tables_NLSF_CB0_16.c","src/src/SKP_Silk_tables_NLSF_CB1_10.c","src/src/SKP_Silk_tables_NLSF_CB1_16.c","src/src/SKP_Silk_tables_gain.c","src/src/SKP_Silk_tables_other.c","src/src/SKP_Silk_tables_pitch_lag.c","src/src/SKP_Silk_tables_pulses_per_block.c","src/src/SKP_Silk_tables_sign.c","src/src/SKP_Silk_tables_type_offset.c","src/src/SKP_Silk_warped_autocorrelation_FIX.c","src/src/signalCompare.c"
      ]
    },
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "<(module_name)" ],
      "copies": [
          {
            "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
            "destination": "<(module_path)"
          }
      ]
    }
  ]
}
